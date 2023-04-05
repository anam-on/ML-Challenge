import numpy as np
import numpy as np
from floyd_warshall import floyd_warshall

def create_dendrogram(graph):
    """
    Create a dendrogram from a graph represented as a dictionary with 'nodes' and 'links' keys.
    """
    # Create adjacency matrix
    n_nodes = len(graph['nodes'])
    adj_matrix = np.zeros((n_nodes, n_nodes))
    for link in graph['links']:
        source = link['source']
        target = link['target']
        adj_matrix[source][target] = 1
        adj_matrix[target][source] = 1

    # Calculate distance matrix using Floyd-Warshall algorithm
    dist_matrix = floyd_warshall(adj_matrix)

    # Perform hierarchical clustering
    dendrogram = hierarchical_clustering(dist_matrix)
    
    return dendrogram
