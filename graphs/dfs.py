graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def dfs(graph, start): 

    visited = []
    stack = []

    visited.append(start)
    stack.append(start)

    while stack: 
        s = stack.pop()
        print(s, end = " ")

        for neighbor in graph[s]: 
            if neighbor not in visited: 
                stack.append(neighbor)
                visited.append(neighbor)

dfs(graph, 'A')