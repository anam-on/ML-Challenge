def normalize_centrality(my_dict):
    """
    The function returns the new dictionary with normalized centrality values.
    """
    min_eig = min(my_dict.values()) # Find and store minimum value 
    max_eig = max(my_dict.values()) # Find and store maximum value
    
    centrality_dict_normalized = {} # Create a new dictionary to store normalized centrality values
    for node in my_dict:
        # For each node in the input dictionary, calculate the normalized centrality value using the formula (centrality - min_centrality) / (max_centrality - min_centrality)
        centrality_dict_normalized[node] = (my_dict[node] - min_eig)/(max_eig - min_eig)
    
    return centrality_dict_normalized