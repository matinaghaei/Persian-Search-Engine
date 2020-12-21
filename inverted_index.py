class InvertedIndex:

    def __init__(self):
        self.postings_lists = {}

    def add_postings_list(self, token, postings_list):
        self.postings_lists[token] = postings_list

    def remove_stop_words(self, threshold):
        keys = list(self.postings_lists.keys())
        for token in keys:
            if self.postings_lists[token].freq > threshold:
                self.postings_lists.pop(token)

    def get_postings_list(self, token):
        if token in self.postings_lists:
            return self.postings_lists[token]
