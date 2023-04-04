from adjacency_matrix import adjacency_matrix
from norm_value import norm_value
import networkx as nx
import numpy as np

def eigenvector_centrality(my_dict, max_iter):
    """
    Returns eigenvector centrality of nodes in a graph
    """
    G = nx.node_link_graph(my_dict)  # create a graph object from the input dictionary using NetworkX
    adjMat = nx.adjacency_matrix(G).todense()  # create the adjacency matrix of the graph and convert it to a dense numpy array
    n = G.number_of_nodes()  # get the number of nodes in the graph
    x = np.ones(n).reshape(n, 1)  # create an initial eigenvector with all elements set to 1
    
    for i in range(max_iter):  # iterate for the given number of iterations
        x = adjMat*x  # update the eigenvector by multiplying it with the adjacency matrix
        x = x/norm_value(x)  # normalize the eigenvector by dividing it by its norm
        result = {}  # create a dictionary to store the centrality scores for each node
        
    i = 0
    for item in my_dict['nodes']:  # iterate over the nodes in the input dictionary
        result[item['id']] = np.asscalar(x[i])  # store the centrality score for the node in the result dictionary
        i += 1
        
    return result  # return the dictionary containing the centrality scores for each node