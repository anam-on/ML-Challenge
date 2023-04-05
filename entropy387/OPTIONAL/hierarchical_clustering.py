def hierarchical_clustering(adj_matrix):
    """
    Performs hierarchical clustering on an adjacency matrix using complete linkage.
    """

    n_nodes = len(adj_matrix)
    clusters = [{node} for node in range(n_nodes)]  # Initialize clusters as individual nodes
    distances = np.array(adj_matrix)

    # Perform hierarchical clustering using complete linkage
    for i in range(n_nodes, 2 * n_nodes - 1):
        min_distance = np.inf
        closest_clusters = ()
        for j in range(i):
            for k in range(j+1, i):
                cluster1 = list(clusters[j])
                cluster2 = list(clusters[k])
                distance = 0
                # Calculate average pairwise distance between nodes in two clusters
                for node1 in cluster1:
                    for node2 in cluster2:
                        distance += distances[node1][node2]
                distance /= len(cluster1) * len(cluster2)
                # Update closest clusters if a smaller distance is found
                if distance < min_distance:
                    min_distance = distance
                    closest_clusters = (j, k)
        # Merge the closest clusters into a new cluster
        merged_cluster = clusters[closest_clusters[0]].union(clusters[closest_clusters[1]])
        clusters.append(merged_cluster)

    dendrogram = [{'node_id': i, 'children': []} for i in range(n_nodes * 2 - 1)]  # Initialize dendrogram
    for i in range(n_nodes, n_nodes * 2 - 1):
        child1, child2 = closest_clusters
        dendrogram[i]['children'] = [child1, child2]  # Update dendrogram with merged clusters as children
        closest_clusters = i, closest_clusters[1]

    return dendrogram
