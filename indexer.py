import math
from inverted_index import InvertedIndex
from postings_list import PostingsList
from positions import Positions


class Indexer:

    def __init__(self, tokens, docs, stopwords_threshold, champion_list_size):
        self.inverted_index = InvertedIndex()
        self.tokens = tokens
        self.docs = docs
        self.build()
        self.inverted_index.remove_stop_words(stopwords_threshold)
        self.calculate_tf_idf()
        self.build_champion_lists(champion_list_size)

    def build(self):
        self.tokens.sort()
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i][0]
            postings_list = PostingsList(token, self.tokens[i][1])
            j = i + 1
            while j < len(self.tokens) and token == self.tokens[j][0]:
                postings_list.add_document(self.tokens[j][1])
                j += 1
            self.inverted_index.add_postings_list(token, postings_list)
            i = j

    def print_doc_list(self, token):
        postings_list = self.inverted_index.get_postings_list(token)
        if postings_list:
            print('postings list of', token, end=' : ')
            for positions in postings_list:
                print('doc', end='')
                print(positions.doc_id, end=' ')
            print()

    def print_inverted_index(self):
        for token, postings_list in self.inverted_index.postings_lists.items():
            print('Token:', token, 'Freq:', postings_list.freq)
            for positions in postings_list.documents:
                print(positions.doc_id, ": ", sep='', end='')
                for pos in positions.position_list:
                    print(pos, end=' ')
                print()
            print()

    def calculate_tf_idf(self):
        number_of_docs = self.docs.get_size()
        for postings_list in self.inverted_index.get_postings_lists():
            term = postings_list.token
            doc_freq = postings_list.get_doc_freq()
            idf = math.log10(number_of_docs / doc_freq)
            for positions in postings_list.documents:
                tf = 1 + math.log10(positions.get_size())
                self.docs.get_doc(positions.doc_id).add_tf_idf(term, tf * idf)

    def build_champion_lists(self, size):
        for postings_list in self.inverted_index.get_postings_lists():
            docs = postings_list.documents.copy()
            Positions.sort_by_id = False
            docs.sort(reverse=True)
            docs = docs[:size]
            Positions.sort_by_id = True
            docs.sort()
            postings_list.add_to_champion(docs)
