import math
import os
from documents import Documents
from indexer import Indexer
from query_processor import QueryProcessor
from tokenizer import Tokenizer


def read_files(directory, docs):
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            f = open(os.path.join(directory, file), mode="r", encoding="utf-8")
            entire_text = f.read()
            f.close()
            docs.add(file.replace('.txt', ''), entire_text)


class Cluster:

    def __init__(self, category, stopwords_threshold, champion_list_size):
        self.category = category
        docs = Documents()
        read_files(f"Wikipedia Clusters/{category}/", docs)
        tokenizer = Tokenizer(docs)
        indexer = Indexer(tokenizer.positionals, docs,
                          stopwords_threshold=stopwords_threshold,
                          champion_list_size=champion_list_size)
        self.center = docs.calculate_center()
        self.center_length = self.calculate_center_length()
        self.query_processor = QueryProcessor(indexer.inverted_index, docs)

    def search(self, query, top):
        results = self.query_processor.search(query, top=top)
        return results

    def calculate_similarity(self, query_tf):
        similarity = 0
        for term, tf in query_tf.items():
            if term in self.center:
                similarity += self.center[term] * tf
        return similarity / self.center_length

    def calculate_center_length(self):
        length = 0
        for val in self.center.values():
            length += val * val
        return math.sqrt(length)
