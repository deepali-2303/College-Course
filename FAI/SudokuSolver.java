import java.util.ArrayList;
import java.util.HashMap;

public class SudokuSolver {

    public static void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            if (i % 3 == 0 && i != 0) {
                System.out.println("- - - - - - - - - - - - - ");
            }
            for (int j = 0; j < board[0].length; j++) {
                if (j % 3 == 0 && j != 0) {
                    System.out.print(" | ");
                }
                if (j == 8) {
                    System.out.println(board[i][j]);
                } else {
                    System.out.print(board[i][j] + " ");
                }
            }
        }
    }

    public static int[] findEmpty(int[][] board) {
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 0) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }

    public static boolean solve(int[][] board) {
        int[] find = findEmpty(board);
        if (find == null) {
            return true;
        } else {
            int row = find[0];
            int col = find[1];
            for (int i = 1; i <= 9; i++) {
                if (valid(board, i, row, col)) {
                    board[row][col] = i;
                    if (solve(board)) {
                        return true;
                    }
                    board[row][col] = 0;
                }
            }
            return false;
        }
    }

    public static boolean valid(int[][] board, int num, int row, int col) {
        // Check row
        for (int i = 0; i < board[0].length; i++) {
            if (board[row][i] == num && col != i) {
                return false;
            }
        }
        // Check column
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] == num && row != i) {
                return false;
            }
        }
        // Check box
        int boxRow = row - row % 3;
        int boxCol = col - col % 3;
        for (int i = boxRow; i < boxRow + 3; i++) {
            for (int j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] == num && i != row && j != col) {
                    return false;
                }
            }
        }
        return true;
    }

    public static ArrayList<int[]> findEmptySpaces(int[][] board) {
        ArrayList<int[]> list = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 0) {
                    int[] empty = {i, j};
                    list.add(empty);
                }
            }
        }
        return list;
    }

    public static void main(String[] args) {
        int[][] board = {
                {7, 8, 0, 4, 0, 0, 1, 2, 0},
                {6, 0, 0, 0, 7, 5, 0, 0, 9},
                {0, 0, 0, 6, 0, 1, 0, 7, 8},
                {0, 0, 7, 0, 4, 0, 2, 6, 0},
                {0, 0, 1, 0, 5, 0, 9, 3, 0},
                {9, 0, 4, 0, 6, 0, 0, 0, 5},
                {0, 7, 0, 3, 0, 0, 0, 1, 2},
                {1, 2, 0, 0, 0, 7, 4, 0, 0},
                {0, 4, 9, 2, 0, 6, 0, 0, 7}
        };

        printBoard(board);
        System.out.println("_______");

        ArrayList<int[]> variables = findEmptySpaces(board);
        HashMap<Integer, ArrayList<Integer>> D = new HashMap<>();
        for (int i = 0; i < variables.size(); i++) {
            ArrayList<Integer> domain = new ArrayList<>();
            for (int j = 1; j <= 9; j++) {
                domain.add(j);
            }
            D.put(i, domain);
            System.out.print("(" + variables.get(i)[0] + ", " + variables.get(i)[1] + ")" + (i != variables.size() - 1 ? ", " : ""));
        }
        System.out.println("\n_______");

        System.out.println("Initial Domain for each variable : {1, 2, 3, 4, 5, 6, 7, 8, 9}");
        System.out.println("_______");

        System.out.println("Constraints : Any two elements of a row or a column or a box cannot be the same.");
        System.out.println("Row constraints : ");
        for (int i = 0; i < 10; i++) {
            System.out.println();
            for (int j = 0; j < variables.size(); j++) {
                if (variables.get(j)[0] == i) {
                    System.out.print("(" + variables.get(j)[0] + ", " + variables.get(j)[1] + ")" + (j != variables.size() - 1 && variables.get(j + 1)[0] == variables.get(j)[0] ? " != " : ""));
                }
            }
        }
        System.out.println("\n_______");

        System.out.println("Column constraints : ");
        for (int i = 0; i < 10; i++) {
            System.out.println();
            for (int j = 0; j < variables.size(); j++) {
                if (variables.get(j)[1] == i) {
                    System.out.print("(" + variables.get(j)[0] + ", " + variables.get(j)[1] + ")" + " != ");
                }
            }
        }
        System.out.println("\n_______");

        System.out.println("Box Constraints : ");
        for (int[] variable : variables) {
            int box_x = variable[1] / 3;
            int box_y = variable[0] / 3;
            for (int i = box_y * 3; i < box_y * 3 + 3; i++) {
                for (int j = box_x * 3; j < box_x * 3 + 3; j++) {
                    if (containsVariable(variables, i, j)) {
                        System.out.print("(" + i + ", " + j + ")" + " != ");
                    }
                }
            }
            System.out.println();
        }
        System.out.println("_______");

        System.out.println("Reduced Constraints for each variable ");
        for (int i = 0; i < variables.size(); i++) {
            for (int j = 1; j <= 9; j++) {
                if (!valid(board, j, variables.get(i)[0], variables.get(i)[1])) {
                    D.get(i).remove(Integer.valueOf(j));
                }
            }
            System.out.println("(" + variables.get(i)[0] + ", " + variables.get(i)[1] + ")" + " : " + D.get(i));
        }
        System.out.println("_______");

        System.out.println("Solution : ");
        solve(board);
        System.out.println("_______");

        printBoard(board);
    }

    public static boolean containsVariable(ArrayList<int[]> variables, int row, int col) {
        for (int[] variable : variables) {
            if (variable[0] == row && variable[1] == col) {
                return true;
            }
        }
        return false;
    }
  }