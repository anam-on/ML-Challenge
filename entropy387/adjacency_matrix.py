def adjacency_matrix(dict): 
    """
    Creates an adjacency matrix of nodes of a graph
    """
    x = {} # Initialize an empty dictionary for the adjacency matrix
    # Loop over all nodes in the graph and add them to the dictionary
    for i in range(len(dict['nodes'])):
        x[dict['nodes'][i]['id']] = [] 
    # Loop over all links in the graph and add them to the adjacency matrix
    for item in dict['links']:
        # Add the target node to the list of neighbors for the source node
        x[item['source']].append(item['target'])
        # Add the source node to the list of neighbors for the target node
        x[item['target']].append(item['source'])
    return x