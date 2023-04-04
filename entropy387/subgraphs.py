from adjacency_matrix import adjacency_matrix

def subgraphs(graph_dict):
    """
    Creates a dictionary of subgraphs of a graph represented as a dictionary of nodes.
    Input variable type should be a dictionary.
    """
    adjMat = adjacency_matrix(graph_dict) # Create an adjacency matrix for the given graph
    visited = set()  # Set to keep track of visited nodes
    subgraph_count = 0  # Counter for subgraphs
    subgraphs = {} # Dictionary to store subgraphs
    
    # Loop over all nodes in the graph
    for node in adjMat:
        # If the node has not been visited yet, it is the start of a new subgraph
        if node not in visited:
            subgraph_count += 1  # Increment the subgraph counter
            # Explore the subgraph using depth-first search
            subgraph = [] # List to store nodes in the current subgraph
            stack = [node]
            while stack:
                current_node = stack.pop() # Take the last node from the stack (LIFO)
                visited.add(current_node) # Add the current node to the set of visited nodes
                subgraph.append(current_node) # Add the current node to the current subgraph
                for neighbor in adjMat[current_node]: # Iterate over neighbors of the current node
                    if neighbor not in visited:
                        stack.append(neighbor)  # If the neighbor has not been visited yet, add the neighbor to the stack to be explored later
            subgraphs[subgraph_count] = subgraph           
    return subgraphs
