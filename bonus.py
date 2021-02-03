from cluster_manager import ClusterManager
from cluster import Cluster


def main():

    physics_cluster = Cluster("Physics", stopwords_threshold=50, champion_list_size=10)
    math_cluster = Cluster("Mathematics", stopwords_threshold=50, champion_list_size=10)
    health_cluster = Cluster("Health", stopwords_threshold=50, champion_list_size=10)
    history_cluster = Cluster("History", stopwords_threshold=50, champion_list_size=10)
    tech_cluster = Cluster("Technology", stopwords_threshold=50, champion_list_size=10)

    cluster_manager = ClusterManager()
    cluster_manager.add_cluster(physics_cluster)
    cluster_manager.add_cluster(math_cluster)
    cluster_manager.add_cluster(health_cluster)
    cluster_manager.add_cluster(history_cluster)
    cluster_manager.add_cluster(tech_cluster)

    running = True
    while running:
        query = input("Enter your query (Or type 'terminate'): ")
        if query == 'terminate':
            running = False
        else:
            results = cluster_manager.search(query, top=5)
            print()
            if len(results) == 0:
                print("No Results :(")
            for i in range(len(results)):
                print(f"{i + 1}. Doc Title : {results[i][0]} \t\t -- \t\t Cosine Score : {results[i][1]}")
            print()


if __name__ == '__main__':
    main()
