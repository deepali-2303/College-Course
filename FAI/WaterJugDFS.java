import java.util.*;

public class WaterJugDFS {
    public static class State {
        int A, B;

        public State(int a, int b) {
            A = a;
            B = b;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null || getClass() != obj.getClass())
                return false;
            State state = (State) obj;
            return A == state.A && B == state.B;
        }

        @Override
        public int hashCode() {
            return Objects.hash(A, B);
        }

        @Override
        public String toString() {
            return "(" + A + ", " + B + ")";
        }
    }

    public static List<String> waterJugDFS(int capacityA, int capacityB, int target) {
        Stack<State> stack = new Stack<>();
        Set<State> visited = new HashSet<>();
        List<String> result = new ArrayList<>();

        State initialState = new State(0, 0);
        stack.push(initialState);

        while (!stack.isEmpty()) {
            State currentState = stack.pop();

            if (currentState.A == target) {
                return result; // Found a solution
            }

            visited.add(currentState);

            // Possible actions: Fill A, Fill B, Pour A to B, Pour B to A, Empty A, Empty B
            State[] actions = {
                    new State(capacityA, currentState.B),
                    new State(currentState.A, capacityB),
                    new State(currentState.A - Math.min(currentState.A, capacityB - currentState.B),
                            currentState.B + Math.min(currentState.A, capacityB - currentState.B)),
                    new State(currentState.A + Math.min(currentState.B, capacityA - currentState.A),
                            currentState.B - Math.min(currentState.B, capacityA - currentState.A)),
                    new State(0, currentState.B),
                    new State(currentState.A, 0)
            };

            for (State action : actions) {
                if (!visited.contains(action)) {
                    stack.push(action);
                    result.add(getActionDescription(currentState, action, capacityA, capacityB));
                }
            }
        }

        return Collections.emptyList(); // No solution found
    }

    public static String getActionDescription(State from, State to, int capacityA, int capacityB) {
        if (from.A < to.A) {
            return "Fill A";
        } else if (from.A > to.A) {
            return "Empty A";
        } else if (from.B < to.B) {
            return "Fill B";
        } else if (from.B > to.B) {
            return "Empty B";
        } else if (from.A != capacityA && from.B != 0) {
            return "Pour B to A";
        } else {
            return "Pour A to B";
        }
    }

    public static void main(String[] args) {
        int capacityA = 4;
        int capacityB = 3;
        int target = 2;

        List<String> solution = waterJugDFS(capacityA, capacityB, target);

        if (!solution.isEmpty()) {
            System.out.println("DFS Traversal of the State Space:");
            for (String action : solution) {
                System.out.println(action);
            }
        } else {
            System.out.println("No solution found.");
        }
    }
}
