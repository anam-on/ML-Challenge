def plot_dendrogram(dendrogram):
    """
    This function plots a dendrogram
    """
    plt.figure(figsize=(10, 5))
    plt.title("Dendrogram")
    plt.xlabel("Node ID")
    plt.ylabel("Distance")
    for i in range(len(dendrogram)):
        node_id = dendrogram[i]['node_id']
        children = dendrogram[i]['children']
        for child in children:
            plt.plot([node_id, node_id], [dendrogram[child]['node_id'], dendrogram[child]['node_id']], 'k-')
            plt.plot([node_id, dendrogram[child]['node_id']], [dendrogram[child]['node_id'], dendrogram[child]['node_id']], 'k-')
    plt.show()

