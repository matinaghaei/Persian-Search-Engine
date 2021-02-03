import math
from tokenizer import tokenize
from max_heap import MaxHeap


def calculate_tf(query):
    terms_freq = {}
    tokens = tokenize(query)
    for token in tokens:
        if token in terms_freq:
            terms_freq[token] += 1
        else:
            terms_freq[token] = 1
    query_tf = {}
    for k, v in terms_freq.items():
        query_tf[k] = 1 + math.log10(v)
    return query_tf


class QueryProcessor:

    def __init__(self, inverted_index, docs):
        self.inverted_index = inverted_index
        self.docs = docs

    def search(self, query, top):
        query_tf = calculate_tf(query)
        results = self.calculate_docs_scores(query_tf)
        max_heap = MaxHeap(len(results))
        return max_heap.select_top(results, top)

    def calculate_docs_scores(self, query_tf):
        scores = {}
        for term, tf in query_tf.items():
            postings_list = self.inverted_index.get_postings_list(term)
            if postings_list:
                for positions in postings_list.champion_list:
                    doc = self.docs.get_doc(positions.doc_id)
                    score = doc.tf_idf_vector[term] * tf
                    if doc.id in scores:
                        scores[doc.id] += score
                    else:
                        scores[doc.id] = score

        for doc_id in scores.keys():
            doc = self.docs.get_doc(doc_id)
            scores[doc_id] /= doc.get_vector_length()
        return scores.items()
