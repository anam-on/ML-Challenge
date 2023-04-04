def degree_count(dict):
    """
    Returns a degree count for every node in a dictionary
    """
    # Initialize an empty dictionary to keep track of degrees of each node
    x =  {}
    # Loop over all nodes in the graph and add them to the dictionary with degree 0
    for i in range(len(dict['nodes'])):
        # We use IDs as keys
        x[dict['nodes'][i]['id']] = 0 
        
    # Loop over all links in the graph
    for item in dict['links']:
        # Increment the degree of the source node by 1
        x[item['source']] = x[item['source']] + 1
        # Increment the degree of the target node by 1
        x[item['target']] = x[item['target']] + 1 
    # Return the dictionary with degrees of each node
    return x