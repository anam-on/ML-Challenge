from adjacency_matrix import adjacency_matrix
def get_isolates(dict):
    """
    Returns a list of isolated nodes of a graph
    """
    adjMat = adjacency_matrix(dict) # Create an adjacency matrix for the given graph
    isolatedNodes = [] # List to store isolated nodes

    # Loop over all nodes in the graph
    for x in adjMat:
        if not adjMat.get(x): # If the node is not connected to any other node
            isolatedNodes.append(x) # Add the node to the list of isolated nodes

    return isolatedNodes # Return the list of isolated nodes
