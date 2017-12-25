graph = {"A": ["B", "D"],
         "B": ["A","C"],
         "C": ["B"],
         "D": ["A","E"],
         "E": ["D"]}

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

print(dolzine(graph))
def bliznjica(graph):
    m = (0,0,99999999999999) #Trojica bližnjica, skupna razdalja
    povezave = [] #seznam preverjenih povezav
    for i in range(0,len(k)):
        for j in range(0,len(k)):
            if k[j] not in graph.get(k[i]) and k[j] != k[i]: #če povezave še ni oz različne točke
                if (k[i],k[j]) not in povezave:
                    graph[k[i]].append(k[j]) #dodamo nove povezave, graf neusmerjen
                    graph[k[j]].append(k[i])
                    dol = dolzine(graph)  #izračunamo nove razdalje
                    graph[k[i]].remove(k[j])   #izbrišemo bližnjico
                    graph[k[j]].remove(k[i])                    
                    povezave.append((k[i],k[j])) #dodamo bližnjico med že preverjene
                    povezave.append((k[j],k[i]))

                    if dol < m[2]:   #preverimo če je nova bližnjica boljša
                        m = (k[j],k[i], dol)
    return(m)

                
    
print(bliznjica(graph))

#Kodo je treba še izboljšati, samo osnutek
m2 = (0,0,0,0,99999999999999)
preverjene = []
for i in range(0, len(k)):
    for j in range(0,len(k)):
                   for s in range(0, len(k)):
                       for l in range(0,len(k)):
                           if k[s] not in graph.get(k[i]):
                               if k[l] not in graph.get(k[j]):
                                   if k[i] != k[s]:
                                       if (k[i], k[l],k[s],k[j]) not in preverjene:
                                           dic = graph
                                           graph[k[i]].append(k[s])
                                           graph[k[j]].append(k[l])
                                           dol = dolzine(graph)
                                           preverjene.append((k[i],k[j],k[s],k[l]))
                                           preverjene.append((k[j],k[i],k[s],k[l]))
                                           preverjene.append((k[i],k[j],k[l],k[s]))
                                           preverjene.append((k[j],k[i],k[l],k[s]))
                                           graph = dic
                                           print(m2)
                                           if dol < m2[4]:
                                               m2 = (k[i],k[s],k[j],k[l],dol)
print(m2)
print(preverjene)
