import java.util.*;

class exp2 {
    int V;

    LinkedList<Integer> l[];
    List<Integer> openList;
    List<Integer> closedList;
    // int[] parent;
    int[] cost;
    int[] heuristic;
    int[] fCost;

    void addEdge(int v, int w, int c) {
        l[v].add(w);
        cost[v * V + w] = c;
    }

    void addHeuristic(int v, int h) {
        heuristic[v] = h;
    }

    exp2(int v) {
        V = v;
        l = new LinkedList[v + 1];
        for (int i = 0; i <= v; i++) {
            l[i] = new LinkedList<>();
        }
        openList = new ArrayList<>();
        closedList = new ArrayList<>();
        cost = new int[(v + 1) * (v + 1)];
        heuristic = new int[v + 1];
        fCost = new int[v + 1];
        // parent = new int[v + 1];
        // Arrays.fill(parent, -1);
    }

    void printLists() {
        System.out.println("\nOpen List: ");
        for (Integer node : openList) {
            System.out.print(fCost[node] + " ");
        }
        System.out.println("\nClosed List: ");
        for (Integer node : closedList) {
            System.out.print(fCost[node] + " ");
        }
        System.out.println();
    }
    

  

    int AStar(int start, int target) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(node -> fCost[node]));
        boolean nodes[] = new boolean[V + 1];
        int[] gCost = new int[V + 1]; 
    
        pq.add(start);
        openList.add(start);
        nodes[start] = true;
       
        gCost[start] = 0;
    
        while (!pq.isEmpty()) {
            int n = pq.poll();
            closedList.add(n);
            openList.remove(Integer.valueOf(n));
            System.out.print(n + ". ");
    
            if (n == target) {
                return fCost[n];
            }
    
            for (int a : l[n]) {
                if (!nodes[a]) {
                    gCost[a] = gCost[n] + cost[n * V + a]; 
                    fCost[a] = gCost[a] + heuristic[a]; 
                    nodes[a] = true;
                    pq.add(a);
                    openList.add(a);
                    // parent[a] = n;
                }
            }
    
            printLists();
        }
    
        return -1;
    }
    

    public static void main(String args[]) {
        exp2 g = new exp2(12);

        g.addEdge(1, 2, 2);
        g.addEdge(1, 5, 1);
        g.addEdge(2, 3, 1);
        g.addEdge(2, 6, 3);
        g.addEdge(3, 4, 2);
        g.addEdge(4, 8, 1);
        g.addEdge(5, 9, 1);
        g.addEdge(6, 5, 5);
        g.addEdge(6, 7, 1);
        g.addEdge(6, 10, 4);
        g.addEdge(7, 3, 3);
        g.addEdge(7, 11, 10);
        g.addEdge(8, 7, 5);
        g.addEdge(8, 12, 5);
        g.addEdge(9, 10, 8);
        g.addEdge(10, 11, 3);
        g.addEdge(11, 12, 1);

        g.addHeuristic(1, 12);
        g.addHeuristic(2, 10);
        g.addHeuristic(3, 16);
        g.addHeuristic(4, 15);
        g.addHeuristic(5, 12);
        g.addHeuristic(6, 7);
        g.addHeuristic(7, 11);
        g.addHeuristic(8, 15);
        g.addHeuristic(9, 11);
        g.addHeuristic(10, 4);
        g.addHeuristic(11, 1);
        g.addHeuristic(12, 0);

        System.out.println("The A* Traversal:");

        int fCost_12 = g.AStar(1, 12);

        System.out.println("\n\nOpen List: " + g.openList);
        System.out.println("Closed List: " + g.closedList+ "\n");

        if (fCost_12 != -1) {
            System.out.println("\nNode 12 has fCost: " + fCost_12);
        } else {
            System.out.println("\nNode 12 is not reachable.");
        }

    
    }
}
