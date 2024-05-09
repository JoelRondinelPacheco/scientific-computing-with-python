my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    print(unvisited)
    print(distances)
    print(paths)
    current = min(unvisited, key=distances.get)
    print(current)
    #while unvisited:
     #   current = min(unvisited, key=distances.get)
    for node, distance in graph[current]:
        print("FOr")
        print('Current graph:', graph[current])
        print('Node for:', node)
        print('Distance for:', distance)
        print('distances[current]:',distances[current])
        print('distances[node]:', distances[node])
        
        #if distance + distances[current] < distances[node]:
         #   pass
        
shortest_path(my_graph, 'A')