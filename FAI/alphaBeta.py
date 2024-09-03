def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif '-' not in board:
        return 0
    else:
        return 0  # Return 0 for games still in progress

def check_winner(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return True
    return False

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

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

def find_best_move(board):
    best_move = -1
    max_eval = float('-inf')
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            eval = alpha_beta_pruning(board, 1, float('-inf'), float('inf'), False)
            board[i] = '-'
            if eval > max_eval:
                max_eval = eval
                best_move = i
    return best_move

def alpha_beta_pruning(board, depth, alpha, beta, is_max_player):
    if depth == 0 or evaluate(board) is not None:
        return evaluate(board)

    if is_max_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def get_suggested_move(board):
    board_copy = board.copy()
    best_move = find_best_move(board_copy)
    return best_move

# Main game loop
board = ['-'] * 9
while True:
    print_board(board)

    user_input = user_move(board)
    board[user_input] = 'O'

    if check_winner(board, 'O'):
        print_board(board)
        print("You win!")
        break
    elif '-' not in board:
        print_board(board)
        print("It's a draw!")
        break

    ai_move = find_best_move(board)
    board[ai_move] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("AI wins!")
        break

    suggested_move = get_suggested_move(board)
    print(f"Suggested move: {suggested_move + 1}\n")
