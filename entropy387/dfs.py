def dfs(node_key, visited, adjMat):
    """
    Performs a depth-first search (DFS) on the given graph starting at the node specified by 'node_key'.
    """
    visited[node_key] = True 
    for adj_node in adjMat[node_key]: # Iterate over the list of adjacent nodes to the current node in the adjacency matrix adjMat.
        if not visited[adj_node]:
            dfs(adj_node, visited, adjMat) # If an adjacent node adj_node has not been visited yet the dfs function is called recursively with 'adj_node' as the new 'node_key'. 
    return visited
