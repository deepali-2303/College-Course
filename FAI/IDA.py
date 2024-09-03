FLAG = False
PATH = []
F_NEW = 10**7


def F_cost(u, s, adj, f_cost, nodes): 
    i = nodes.index(s) 
    y = 0 

    for x in range(len(adj[s][1])):
        if adj[s][1][x][0]==u:
            y = x
            break

    s_gcost = f_cost[i] - adj[s][0]
    g = s_gcost + adj[s][1][y][1] 
    h = adj[u][0] 
    f = g + h
    return f

def backtrack(s, adj, f_cost, nodes, path, f_values):
    global F_NEW
    F_NEW = 10**7

    global FLAG

    global PATH

    l = IDA_star(s, '', adj, f_values[0], f_values[1], f_cost, nodes, path)
    print('f_bound, f_new:', l[3], l[4])
    
    if FLAG:
        print('\n')
        print('Final path: ', PATH)
        print('Cost to reach goal state: ', f_cost[7])
        print('Goal state reached. End of program.')
    else:
        backtrack(s, adj, f_cost, nodes, [], [l[4], 10**7])


def IDA_star(s, u, adj, f_bound, f_new, f_cost, nodes, path):
    global F_NEW

    global FLAG

    global PATH
    if s!='S':
        f = F_cost(s, u, adj, f_cost, nodes)
    else:
        
        print('New Iteration - ')
        f = f_cost[0]

    if f > f_bound:
        f_new = min(f, f_new)
        F_NEW = min(F_NEW, f_new)

        print('Current node: ', s)
        print('F-limit: ', f_bound, '\tF-new: ', F_NEW)
        print('Path:', path)
        print()

        l = [s, '', adj, f_bound, F_NEW, f_cost, nodes, path]
        return l
    
    else: 
        path.append(s)

        print('Current node: ', s)
        print('F-limit: ', f_bound, '\tF-new: ', F_NEW)
        print('Path:', path)
        print()

        i = nodes.index(s)
        f_cost[i] = f

        if s=='G':    
            FLAG = True
            PATH = path.copy()
            l = [s, 'G', adj, f_bound, F_NEW, f_cost, nodes, path]
            return l
        
        else:
            for k in range(len(adj[s][1])):

                if f!=f_bound and f>f_bound:
                    f_new = min(f, f_new)
                    F_NEW = min(F_NEW, f_new)
                else:
                    f_new = f_new

                l = IDA_star(adj[s][1][k][0], s, adj, f_bound, F_NEW, f_cost, nodes, path)

                if adj[s][1][k][0] in path:
                    path.pop(-1)
                
                if FLAG:
                    l = [s, 'G', adj, f_bound, F_NEW, f_cost, nodes, path]
                    return l

            l = [adj[s][1][k][0], s, adj, l[3], l[4], f_cost, nodes, path]
            return  l


adj = {
    'S': [6, [['A', 2], ['B', 3]]],
    'A': [4, [['C', 3]]],
    'B': [4, [['C', 1], ['D', 3]]],
    'C': [4, [['D', 1], ['E', 3]]],
    'D': [3.5, [['F', 2]]],
    'E': [1, [['G', 2]]],
    'F': [1, [['G', 1]]],
    'G': [0]
}
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
f_cost = [10**7 for i in range(8)]
s = input('Enter the start node\n').upper()
f_cost[0] = adj[s][0]
path = []
f_values = [0, 10**7] 
backtrack(s, adj, f_cost, nodes, path, f_values)

