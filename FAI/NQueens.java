import java.util.Random;

public class NQueens {
    static int N; 
    static int[] board; 
    // static Random random = new Random();
    // Random random = new Random(System.nanoTime());


    static void initializeBoard() {
      // random = new Random();
      Random random = new Random(System.nanoTime());
      for (int i = 0; i < N; i++) {
          
          board[i] = random.nextInt(N);
      }
  }

   
    static int calculateHeuristic() {
        int heuristic = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (board[i] == board[j] || Math.abs(i - j) == Math.abs(board[i] - board[j])) {
                    heuristic++;
                }
            }
        }
        return heuristic;
    }

  
    static void printBoardWithHeuristics() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i] == j) {
                    System.out.print("Q ");
                } else {
                    int temp = board[i]; 
                    board[i] = j;
                    int heuristic = calculateHeuristic();
                    System.out.print(String.format("%2d ", heuristic)); 
                    board[i] = temp; 
                }
            }
            System.out.println();
        }
    }

  
    static void hillClimbing() {
        int currentHeuristic = calculateHeuristic();
        int restarts = 0;

        System.out.println("Initial board:");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i] == j ? "Q " : "- ");
            }
            System.out.println();
        }
        // printBoardWithHeuristics();
        System.out.println("Initial board heuristic: " + currentHeuristic);
        System.out.println("\nInitial board heuristic values:");
        printBoardWithHeuristics();

        while (currentHeuristic > 0) {
            int minHeuristic = currentHeuristic;
            int[] bestMove = new int[N];

            for (int i = 0; i < N; i++) {
                int originalColumn = board[i];

                for (int j = 0; j < N; j++) {
                    board[i] = j;
                    int newHeuristic = calculateHeuristic();

                    if (newHeuristic < minHeuristic) {
                        minHeuristic = newHeuristic;
                        System.arraycopy(board, 0, bestMove, 0, N);
                    }
                }

                board[i] = originalColumn;
            }

            if (minHeuristic >= currentHeuristic) {
                initializeBoard();
                currentHeuristic = calculateHeuristic();
                restarts++;
            } else {
                System.arraycopy(bestMove, 0, board, 0, N);
                currentHeuristic = minHeuristic;
            }

            System.out.println("\nBoard after restart " + restarts + ":");
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.print(board[i] == j ? "Q " : "- ");
                }
                System.out.println();
            }

            System.out.println("Board heuristic after restart " + restarts + ": " + currentHeuristic);
            System.out.println("Board heuristic values after restart " + restarts + ":");
            printBoardWithHeuristics();
        }

        System.out.println("\nSolution found after " + restarts + " restart(s).");

        System.out.println("\nFinal solution board:");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i] == j ? "Q " : "- ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        N = 8;
        board = new int[N];
        // random.setSeed(System.currentTimeMillis());

        hillClimbing();
    }
}
