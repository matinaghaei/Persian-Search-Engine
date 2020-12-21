from inverted_index import InvertedIndex
from postings_list import PostingsList


class Indexer:

    def __init__(self, tokens, stopwords_threshold):
        self.inverted_index = InvertedIndex()
        self.tokens = tokens
        self.build()
        self.inverted_index.remove_stop_words(stopwords_threshold)

    def build(self):
        self.tokens.sort()
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i][0]
            postings_list = PostingsList(self.tokens[i][1])
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
                print(positions.doc, end=' ')
            print()

    def print_inverted_index(self):
        for token, postings_list in self.inverted_index.postings_lists.items():
            print('Token:', token, 'Freq:', postings_list.freq)
            for positions in postings_list.documents:
                print(positions.doc, ": ", sep='', end='')
                for pos in positions.position_list:
                    print(pos, end=' ')
                print()
            print()
