from query_processor import calculate_tf


class ClusterManager:

    def __init__(self):
        self.clusters = []

    def add_cluster(self, cluster):
        self.clusters.append(cluster)

    def search(self, query, top):
        query_tf = calculate_tf(query)
        best_cluster = None, 0
        for cluster in self.clusters:
            similarity = cluster.calculate_similarity(query_tf)
            if similarity > best_cluster[1]:
                best_cluster = cluster, similarity
        results = best_cluster[0].search(query, top)
        return results
