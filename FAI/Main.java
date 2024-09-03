import java.util.Stack;

public class Main {
    public static class State {
        int jugA;
        int jugB;

        public State(int jugA, int jugB) {
            this.jugA = jugA;
            this.jugB = jugB;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            State state = (State) obj;
            return jugA == state.jugA && jugB == state.jugB;
        }

        @Override
        public int hashCode() {
            return Objects.hash(jugA, jugB);
        }

        @Override
        public String toString() {
            return "(" + jugA + ", " + jugB + ")";
        }
    }

    public static void waterJugDFS(State initialState, State goalState) {
        Stack<State> stack = new Stack<>();
        Set<State> visited = new HashSet<>();

        stack.push(initialState);

        while (!stack.isEmpty()) {
            State currentState = stack.pop();
            visited.add(currentState);

            // Check if the goal state is reached
            if (currentState.equals(goalState)) {
                System.out.println("Solution found: " + currentState);
                return;
            }

            // Generate possible actions
            List<State> actions = generateActions(currentState);

            for (State action : actions) {
                if (!visited.contains(action)) {
                    stack.push(action);
                }
            }
        }

        System.out.println("No solution found.");
    }

    public static List<State> generateActions(State currentState) {
        List<State> actions = new ArrayList<>();

        // Fill Jug A from the pump
        if (currentState.jugA < 4) {
            State nextState = new State(4, currentState.jugB);
            actions.add(nextState);
        }

        // Fill Jug B from the pump
        if (currentState.jugB < 3) {
            State nextState = new State(currentState.jugA, 3);
            actions.add(nextState);
        }

        // Pour water from Jug A to Jug B
        if (currentState.jugA > 0 && currentState.jugB < 3) {
            int pourAmount = Math.min(currentState.jugA, 3 - currentState.jugB);
            State nextState = new State(currentState.jugA - pourAmount, currentState.jugB + pourAmount);
            actions.add(nextState);
        }

        // Pour water from Jug B to Jug A
        if (currentState.jugB > 0 && currentState.jugA < 4) {
            int pourAmount = Math.min(currentState.jugB, 4 - currentState.jugA);
            State nextState = new State(currentState.jugA + pourAmount, currentState.jugB - pourAmount);
            actions.add(nextState);
        }

        // Empty Jug A
        if (currentState.jugA > 0) {
            State nextState = new State(0, currentState.jugB);
            actions.add(nextState);
        }

        // Empty Jug B
        if (currentState.jugB > 0) {
            State nextState = new State(currentState.jugA, 0);
            actions.add(nextState);
        }

        return actions;
    }

    public static void main(String[] args) {
        State initialState = new State(0, 0);
        State goalState = new State(2, 0);

        System.out.println("DFS Traversal and Solution Path:");
        waterJugDFS(initialState, goalState);
    }
}
