import java.util.ArrayList;
import java.util.Arrays;

class Node {
    int[][] state;
    int cost;
    Node parent;
    int heuristic;

    public Node(int[][] state, int cost, Node parent, int heuristic) {
        this.state = state;
        this.cost = cost;
        this.parent = parent;
        this.heuristic = heuristic;
    }
}

public class IDAStar {
    private static int[][] goalState = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

    public static void main(String[] args) {
        int[][] initialState = {{2, 8, 1},
                                {0, 4, 3},
                                {7, 6, 5}};

        Node initialNode = new Node(initialState, 0, null, calculateHeuristic(initialState));

        int threshold = initialNode.heuristic;

        while (true) {
            Result result = search(initialNode, 0, threshold);
            if (result.isGoalFound()) {
                printSolution(result.getNode());
                break;
            }
            if (result.getNewThreshold() == Integer.MAX_VALUE) {
                System.out.println("Goal state not found.");
                break;
            }
            threshold = result.getNewThreshold();
        }
    }

   private static Result search(Node node, int cost, int threshold) {
        int f = cost + node.heuristic;
        if (f > threshold) {
            return new Result(false, f);
        }
        if (Arrays.deepEquals(node.state, goalState)) {
            return new Result(true, f, node);
        }

        int min = Integer.MAX_VALUE;

        ArrayList<Node> neighbors = generateNeighbors(node);
        for (Node neighbor : neighbors) {
            Result result = search(neighbor, cost + 1, threshold);
            if (result.isGoalFound()) {
                return result;
            }

            if (result.getNewThreshold() < min) {
                min = result.getNewThreshold();
            }
        }

        return new Result(false, min);
    }

    private static ArrayList<Node> generateNeighbors(Node node) {
        ArrayList<Node> neighbors = new ArrayList<>();

        int[][] state = node.state;
        int row = 0;
        int col = 0;

        // Find the position of the empty tile (0)
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (state[i][j] == 0) {
                    row = i;
                    col = j;
                }
            }
        }

        // Generate new states by moving the empty tile
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] dir : directions) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
                int[][] newState = new int[3][3];
                for (int i = 0; i < 3; i++) {
                    newState[i] = Arrays.copyOf(state[i], 3);
                }
                newState[row][col] = newState[newRow][newCol];
                newState[newRow][newCol] = 0;

                Node newNode = new Node(newState, node.cost + 1, node, calculateHeuristic(newState));
                neighbors.add(newNode);
            }
        }

        return neighbors;
    }

    private static int calculateHeuristic(int[][] state) {
        int heuristic = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (state[i][j] != goalState[i][j]) {
                    heuristic++;
                }
            }
        }

        return heuristic;
    }

    private static void printSolution(Node node) {
        ArrayList<Node> path = new ArrayList<>();
        while (node != null) {
            path.add(0, node);
            node = node.parent;
        }

        for (Node n : path) {
            for (int[] row : n.state) {
                System.out.println(Arrays.toString(row));
            }
            System.out.println();
        }
    }

    private static class Result {
        private boolean goalFound;
        private int newThreshold;
        private Node node;

        public Result(boolean goalFound, int newThreshold) {
            this.goalFound = goalFound;
            this.newThreshold = newThreshold;
        }

        public Result(boolean goalFound, int newThreshold, Node node) {
            this.goalFound = goalFound;
            this.newThreshold = newThreshold;
            this.node = node;
        }

        public boolean isGoalFound() {
            return goalFound;
        }

        public int getNewThreshold() {
            return newThreshold;
        }

        public Node getNode() {
            return node;
        }
    }
}
