import java.util.ArrayList;
import java.util.HashMap;

class Astar {

    static int[] heuristicCost = {12, 10, 16, 15, 12, 7, 11, 15, 11, 4, 1, 0};
    static int goalState = 12;

    public static int calculateCost(int u, int k, int[] heuristicCost, HashMap<Integer, ArrayList<int[]>> adjList, ArrayList<Integer> openList, int[] totalCost) {
        int i = 0;
        for (int j = 0; j < adjList.get(u).size(); j++) {
            if (adjList.get(u).get(j)[0] == k) {
                i = j;
                break;
            }
        }
        int uGCost = totalCost[u - 1] - heuristicCost[u - 1];
        int kGCost = adjList.get(u).get(i)[1];
        int g = uGCost + kGCost;
        int h = heuristicCost[k - 1];
        return g + h;
    }

    public static int findMinimumNode(ArrayList<Integer> openList, int[] totalCost, int[] heuristicCost) {
        int val = Integer.MAX_VALUE;
        int minNode = 0;
        for (int i : openList) {
            if (val > totalCost[i - 1]) {
                val = totalCost[i - 1];
                minNode = i;
            } else if (val == totalCost[i - 1]) {
                int g1 = totalCost[i - 1] - heuristicCost[i - 1];
                int g2 = totalCost[minNode - 1] - heuristicCost[minNode - 1];
                if (g1 < g2) {
                    minNode = i;
                }
            }
        }
        return minNode;
    }

    public static void aStarSearch(int startNode, HashMap<Integer, ArrayList<int[]>> adjList) {
        ArrayList<Integer> openList = new ArrayList<>();
        int[] totalCost = new int[12];
        ArrayList<Integer> closedList = new ArrayList<>();
        boolean isGoalReached = false;

        for (int i = 0; i < 12; i++) {
            totalCost[i] = Integer.MAX_VALUE;
        }
        totalCost[startNode - 1] = heuristicCost[startNode - 1];
        openList.add(startNode);

        System.out.println("Open List: " + openList);
        System.out.println("Closed List: " + closedList);
        System.out.println();

        while (!openList.isEmpty()) {
            int minNode = findMinimumNode(openList, totalCost, heuristicCost);
            int u = minNode;
            openList.remove(Integer.valueOf(u));
            closedList.add(u);

            for (int k = 0; k < adjList.get(u).size(); k++) {
                int[] x = adjList.get(u).get(k);

                if (!closedList.contains(x[0]) && !openList.contains(x[0])) {
                    openList.add(x[0]);
                    totalCost[x[0] - 1] = calculateCost(u, x[0], heuristicCost, adjList, openList, totalCost);
                }

                if (x[0] == goalState) {
                    System.out.println("Goal state reached");
                    System.out.println("Open List: " + openList);
                    System.out.println("Closed List: " + closedList);
                    System.out.println();
                    System.out.println("Number of nodes in open list: " + openList.size());
                    System.out.println("Number of nodes in closed list: " + closedList.size());
                    isGoalReached = true;
                    openList.clear();
                    break;
                }
            }

            if (isGoalReached) {
                break;
            }

            System.out.println("Open List: " + openList);
            System.out.println("Closed List: " + closedList);
            System.out.println();
        }
    }

    public static void main(String[] args) {
        HashMap<Integer, ArrayList<int[]>> adjList = new HashMap<>();
        adjList.put(1, new ArrayList<>());
        adjList.get(1).add(new int[]{2, 2});
        adjList.get(1).add(new int[]{5, 1});

        adjList.put(2, new ArrayList<>());
        adjList.get(2).add(new int[]{3, 1});
        adjList.get(2).add(new int[]{6, 3});

        adjList.put(3, new ArrayList<>());
        adjList.get(3).add(new int[]{4, 2});

        adjList.put(4, new ArrayList<>());
        adjList.get(4).add(new int[]{8, 1});

        adjList.put(5, new ArrayList<>());
        adjList.get(5).add(new int[]{9, 1});

        adjList.put(6, new ArrayList<>());
        adjList.get(6).add(new int[]{5, 5});
        adjList.get(6).add(new int[]{7, 1});
        adjList.get(6).add(new int[]{10, 4});

        adjList.put(7, new ArrayList<>());
        adjList.get(7).add(new int[]{3, 3});
        adjList.get(7).add(new int[]{11, 10});

        adjList.put(8, new ArrayList<>());
        adjList.get(8).add(new int[]{7, 5});
        adjList.get(8).add(new int[]{12, 15});

        adjList.put(9, new ArrayList<>());
        adjList.get(9).add(new int[]{10, 4});

        adjList.put(10, new ArrayList<>());
        adjList.get(10).add(new int[]{11, 3});

        adjList.put(11, new ArrayList<>());
        adjList.get(11).add(new int[]{12, 1});

        adjList.put(12, new ArrayList<>());

        aStarSearch(1, adjList);
    }
}
