from tokenizer import tokenize


class QueryProcessor:

    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def search(self, query):
        relevant_documents = {}
        tokens = tokenize(query)
        for token in tokens:
            postings_list = self.inverted_index.get_postings_list(token)
            if postings_list:
                for positions in postings_list.documents:
                    if positions.doc in relevant_documents:
                        relevant_documents[positions.doc] += 1
                    else:
                        relevant_documents[positions.doc] = 1
        results = sorted(relevant_documents.items(), key=lambda item: item[1], reverse=True)
        return results
