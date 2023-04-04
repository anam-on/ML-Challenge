from adjacency_matrix import adjacency_matrix
from dfs import dfs

def test_graph_connection(dict):
    """
    This function returns a boolean value 'True' if a graph is connected, or false otherwise
    """
    # Create the adjacency matrix for the graph
    adjMat = adjacency_matrix(dict)
    # Get the number of nodes in the graph
    n = len(dict['nodes'])
    
    # Loop over all nodes in the graph
    for i in range(n):
        visited = {}  # Initialize a dictionary to keep track of visited nodes
        # Loop over all nodes in the graph and mark them as unvisited
        for j in range(n):
            visited[dict['nodes'][j]['id']] = False
        # Run depth-first search on the current node
        dfs(dict['nodes'][i]['id'], visited, adjMat)
        # If any node is unvisited after the search, the graph is disconnected
        if False in visited.values():
            return False
    # If all nodes have been visited from every starting node, the graph is connected
    return True