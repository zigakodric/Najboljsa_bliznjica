graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

k = list(graph.keys())

def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


def dolzine(graph):
    s = []
    for i in range(1,len(k)):
        s.append(len(bfs_shortest_path(graph, k[0],k[i]))-1)
    return(sum(s))

def bliznjica(graph):
    se2=[]
    povezave = []
    for i in range(0,len(k)):
        for j in range(0,len(k)):
            if k[j] not in graph.get(k[i]) and k[j] != k[i]:
                if (k[i],k[j]) not in povezave:
                    dic = graph
                    graph[k[i]].append(k[j])
                    graph[k[j]].append(k[i])
                    se2.append((k[j],k[i],dolzine(graph)))
                    graph = dic
                    povezave.append((k[i],k[j]))
                    povezave.append((k[j],k[i]))
                    print(povezave)
                    print(se2)
    return(min(se2))

print(bliznjica(graph))