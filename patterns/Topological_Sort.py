from collections import deque

def topological_sort(vertices, edges):
    sorted_order = []
    
    if vertices <= 0:
        return sorted_order

    # 1. Initialize the In-degree and Adjacency List
    in_degree = {}
    graph = {}
    
    for i in range(vertices):
        in_degree[i] = 0
        graph[i] = []

    # 2. Build the graph and calculate In-degree
    for i in range(len(edges)):
        parent = edges[i][0]
        child = edges[i][1]
        
        graph[parent].append(child)  # Add the neighbor
        in_degree[child] += 1        # Increment the in-degree for the child

    # 3. Find all nodes with In-degree = 0 and add them to the Queue
    sources = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)

    # 4. Iterate and process (BFS)
    while len(sources) > 0:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        # Reduce the In-degree for each child/neighbor of this node
        children = graph[vertex]
        for i in range(len(children)):
            child = children[i]
            in_degree[child] -= 1
            
            # If In-degree becomes 0, add it to the Queue
            if in_degree[child] == 0:
                sources.append(child)

    # If sorted_order doesn't contain all vertices, a cycle exists
    if len(sorted_order) != vertices:
        return []

    return sorted_order