graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def bfs(graph, start): 

    visited = [] # keep track of visited nodes
    queue = [] # to keep track of neighbors to explore

    # enqueue start and preemptively mark visited so it isn't added to queue again. 
    visited.append(start)
    queue.append(start)

    while queue: 
        # pop off the next node to visit (of which the queue only has unvisited nodes)
        s = queue.pop(0)
        print(s, end = " ")
        
        # inspect the neighbors of node s
        for neighbor in graph[s]: 
            
            # if neighbor hasn't been visited, then append to queue to visit and preemptively indicate that it has been visited so you don't add it twice
            if neighbor not in visited: 
                visited.append(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')

