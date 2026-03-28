def dfs(graph, node, visited):
    # Step 1: Check if node already visited
    if node in visited:
        return
    
    # Step 2: Visit the node
    print(node, end=" ")
    visited.add(node)
    
    # Step 3: Visit all neighbors
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


# Main program
if __name__ == "__main__":
    # Graph (Adjacency List Representation)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    visited = set()   # To track visited nodes
    
    start_node = 'A'
    
    print("DFS Traversal:")
    dfs(graph, start_node, visited)