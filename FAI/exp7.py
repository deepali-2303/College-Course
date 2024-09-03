def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return True
    return False


def score_calculation(board):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    score = 0

    for line in lines:
        computer_count = 0
        opponent_count = 0
        empty_count = 0

        for i in line:
            if board[i] == 'X':
                computer_count += 1
            elif board[i] == 'O':
                opponent_count += 1
            else:
                empty_count += 1

        if computer_count == 3:
            score += 100
        elif computer_count == 2 and empty_count == 1:
            score += 10
        elif computer_count == 1 and empty_count == 2:
            score += 1

        if opponent_count == 3:
            score -= 100
        elif opponent_count == 2 and empty_count == 1:
            score -= 10
        elif opponent_count == 1 and empty_count == 2:
            score -= 1

    return score


def alpha_beta_pruning(board, depth, alpha, beta, is_max):
    if depth == 0 or score_calculation(board) != 0:
        return score_calculation(board)

    if is_max:
        max_val = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                val = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                board[i] = '-'
                max_val = max(max_val, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
        return max_val
    else:
        min_val = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                val = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                board[i] = '-'
                min_val = min(min_val, val)
                beta = min(beta, val)
                if beta <= alpha:
                    break
        return min_val


def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == '-':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


board = ["-"] * 9
print_board(board)

while True:
    user_input = user_move(board)
    board[user_input] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break
    elif '-' not in board:
        print_board(board)
        print("It's a draw!")
        break

    best_move = -1
    max_val = float('-inf')

    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            val = alpha_beta_pruning(board, 2, float('-inf'), float('inf'), False)
            board[i] = '-'
            if val > max_val:
                max_val = val
                best_move = i

    board[best_move] = 'O'

    if check_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break

    print_board(board)
