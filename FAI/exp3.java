import java.util.*;

public class exp3 {

    public static void main(String[] args) {
        int[] s = { 0, 0 };
        Set<String> opened = new HashSet<>();
        Set<String> closed = new HashSet<>();
        int[] goal = { 2, 0 };
        int a = 4, b = 3;
        performDFS(s, opened, closed, goal, a, b, 0);
    }

    public static void performDFS(int[] state, Set<String> opened, Set<String> closed, int[] goal, int a, int b, int count) {
        if (closed.contains(getKey(state))) {
            return;
        } else if (state[0] == goal[0] && state[1] == goal[1]) {
            System.out.println("Reached final goal state : " + getKey(state));
            return;
        } else {
            System.out.println();
            System.out.println("Current node : " + getKey(state));
            System.out.println();
            closed.add(getKey(state));

            if (opened.contains(getKey(state))) {
                opened.remove(getKey(state));
            }

            System.out.println("Closed list: " + closed);

            if (state[0] == 0 && state[1] == 0) {
                if (!closed.contains(getKey(new int[] { 4, state[1] }))
                        && !opened.contains(getKey(new int[] { 4, state[1] }))) {
                    opened.add(getKey(new int[] { 4, state[1] }));
                }
                if (!closed.contains(getKey(new int[] { state[0], 3 }))
                        && !opened.contains(getKey(new int[] { state[0], 3 }))) {
                    opened.add(getKey(new int[] { state[0], 3 }));
                }

                System.out.println("Opened list: " +opened);

                int[] newState = { 4, state[1] };
                performDFS(newState, opened, closed, goal, a, b, count);

                newState = new int[] { state[0], 3 };
                performDFS(newState, opened, closed, goal, a, b, count);
            } else if (state[0] == 0 || state[1] == 0) {
                if (state[0] == 0) {
                    int[] newState = { a, state[1] };
                    if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                        opened.add(getKey(newState));
                    }
                    newState = new int[] { 0, 0 };
                    if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                        opened.add(getKey(newState));
                    }
                    newState = new int[] { state[1], 0 };
                    if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                        opened.add(getKey(newState));
                    }

                    System.out.println("Opened list: " + opened);

                    newState = new int[] { a, state[1] };
                    performDFS(newState, opened, closed, goal, a, b, count);

                    newState = new int[] { 0, 0 };
                    performDFS(newState, opened, closed, goal, a, b, count);

                    newState = new int[] { state[1], 0 };
                    performDFS(newState, opened, closed, goal, a, b, count);

                } else if (state[1] == 0) {
                    int[] newState = { 0, 0 };
                    if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                        opened.add(getKey(newState));
                    }
                    newState = new int[] { state[0], b };
                    if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                        opened.add(getKey(newState));
                    }

                    if (state[0] > b) {
                        newState = new int[] { state[0] - b, b };
                        if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                            opened.add(getKey(newState));
                        }

                        System.out.println("Opened list: " + opened);

                        newState = new int[] { 0, 0 };
                        performDFS(newState, opened, closed, goal, a, b, count);

                        newState = new int[] { state[0], b };
                        performDFS(newState, opened, closed, goal, a, b, count);

                        newState = new int[] { state[0] - b, b };
                        performDFS(newState, opened, closed, goal, a, b, count);

                    } else {
                        newState = new int[] { 0, state[0] };
                        if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                            opened.add(getKey(newState));
                        }

                        System.out.println("Opened: " + opened);

                        newState = new int[] { 0, 0 };
                        performDFS(newState, opened, closed, goal, a, b, count);

                        newState = new int[] { state[0], b };
                        performDFS(newState, opened, closed, goal, a, b, count);

                        newState = new int[] { 0, state[0] };
                        performDFS(newState, opened, closed, goal, a, b, count);
                    }
                }
            } else {
                int[] newState = { 0, state[1] };
                if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                    opened.add(getKey(newState));
                }
                newState = new int[] { state[0], 0 };
                if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                    opened.add(getKey(newState));
                }

                int x = Math.min(state[0], b - state[1]);
                // int y = Math.min(a - state[0], state[1]);

                newState = new int[] { state[0] - x, state[1] + x };
                if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                    opened.add(getKey(newState));
                }
                newState = new int[] { a - state[0], state[1] };
                if (!closed.contains(getKey(newState)) && !opened.contains(getKey(newState))) {
                    opened.add(getKey(newState));
                }

                System.out.println("Opened list: " + opened);

                newState = new int[] { 0, state[1] };
                performDFS(newState, opened, closed, goal, a, b, count);

                newState = new int[] { state[0], 0 };
                performDFS(newState, opened, closed, goal, a, b, count);

                newState = new int[] { state[0] - x, state[1] + x };
                performDFS(newState, opened, closed, goal, a, b, count);

                newState = new int[] { a - state[0], state[1] };
                performDFS(newState, opened, closed, goal, a, b, count);
            }
        }
    }

    public static String getKey(int[] state) {
        return "{" +state[0] + "," + state[1] + "}";
    }
}
