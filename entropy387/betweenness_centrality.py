from adjacency_matrix import adjacency_matrix
 
def betweenness_centrality(graph):
    """
    This function implements the Brandes algorithm for calculating betweenness centrality.
    It takes a graph represented as a dictionary as input and returns a dictionary of 
    betweenness centrality scores for each node in the graph.
    """
    # create the adjacency matrix of the graph
    adjMat = adjacency_matrix(graph)
    # initialize betweenness centrality for all nodes to 0
    betweenness = {node: 0.0 for node in adjMat} 

    # Iterate over each node in the graph
    for node in adjMat:
        # initialize data structures for the algorithm
        S = [] # an empty list that will be used to keep track of the nodes
        # in the order they are visited during the breadth-first search
        P = {v: [] for v in adjMat} # a dictionary that will store the predecessors 
        # of each node in the shortest paths from the current node to all other nodes
        sigma = {v: 0 for v in adjMat} # a dictionary that will store the number of 
        # shortest paths from the current node to all other nodes
        sigma[node] = 1 # this is initialized to one because there is a single shortest path
        # from the current node to itself
        d = {v: -1 for v in adjMat} # a dictionary that will store the length of 
        # the shortest path from the current node to all other nodes. This distance is 
        # initialized to -1 to indicate that those notes aren't visited yet
        d[node] = 0 # a distance from the current node to itself is equal to zero

        # perform breadth-first search starting from the current node
        Q = [node]
        while Q: # while loop continues as long as there are nodes in the queue
            v = Q.pop(0) # v is the next node to be visited, which is taken from the front of the queue
            S.append(v) # S is updated to include v in the order it was visited.
            for w in adjMat[v]:
                if d[w] < 0: # if node is not visited
                    Q.append(w)
                    d[w] = d[v] + 1
                if d[w] == d[v] + 1:
                    sigma[w] += sigma[v]
                    P[w].append(v)

        # calculate dependencies of nodes on the current node
        delta = {v: 0 for v in adjMat}
        while S:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != node:
                betweenness[w] += delta[w]

    # normalize betweenness centrality by dividing by (n-1)(n-2)/2
    n = len(adjMat)
    normalization_factor = (n - 1) * (n - 2) # I noticed that if I divide it by 2 as the formula says,
    # I get the results twice as big as those from networkx function, so I omitted dividing by 2
    for node in adjMat:
        betweenness[node] /= normalization_factor

    return betweenness
