import math
from tokenizer import tokenize
from max_heap import MaxHeap


class QueryProcessor:

    def __init__(self, inverted_index, docs):
        self.inverted_index = inverted_index
        self.docs = docs

    def search(self, query, top):
        scores = {}
        terms_freq = {}
        tokens = tokenize(query)
        for token in tokens:
            if token in terms_freq:
                terms_freq[token] += 1
            else:
                terms_freq[token] = 1

        for term, number in terms_freq.items():
            query_tf = 1 + math.log10(number)
            posting_list = self.inverted_index.get_postings_list(term)
            for positions in posting_list.champion_list:
                doc = self.docs.get_doc(positions.doc_id)
                score = doc.tf_idf_vector[term] * query_tf
                if doc.id in scores:
                    scores[doc.id] += score
                else:
                    scores[doc.id] = score

        for doc_id in scores.keys():
            doc = self.docs.get_doc(doc_id)
            scores[doc_id] /= doc.get_vector_length()

        results = scores.items()
        max_heap = MaxHeap(len(results))
        return max_heap.select_top(results, top)
