import numpy as np

def floyd_warshall(adj_matrix):
    """
    Function to calculate the Floyd-Warshall distance matrix
    """
    n = len(adj_matrix)
    dist = np.copy(adj_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist