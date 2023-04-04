from normalize_quality import normalize_quality
from normalize_centrality import normalize_centrality
from eigenvector_centrality import eigenvector_centrality
from betweenness_centrality import betweenness_centrality

def rank_the_nodes(my_dict, w1, w2, w3, w4):
    """
    This function ranks the nodes in a graph based on a weighted sum of various centrality measures and node qualities.
    The input arguments are:
        - my_dict: a dictionary representing a graph
        - w1, w2, w3, w4: weights for different measures, used to calculate the weighted sum for each node
    """
    # The function first normalizes the node qualities and the centrality measures (eigenvector and betweenness)
    new_dict = normalize_quality(my_dict)
    norm_eig_cen = normalize_centrality(eigenvector_centrality(my_dict, 150))
    norm_bet_cen = normalize_centrality(betweenness_centrality(my_dict))
    
    # Calculate the weighted sum for each node using the input weights and the normalized values.
    for item in new_dict['nodes']:
        item['weighted_sum'] = w1*item['q1'] + w2*item['q2'] + w3*norm_eig_cen[item['id']] + w4*norm_bet_cen[item['id']]
    
    # Sort the nodes in descending order based on their weighted sum, and return the sorted list of nodes
    sorted_nodes = sorted(new_dict['nodes'], key=lambda x: x['weighted_sum'], reverse=True)
    return sorted_nodes