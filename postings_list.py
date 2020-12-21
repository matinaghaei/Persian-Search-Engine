class PostingsList:

    def __init__(self, doc):
        self.documents = [doc]
        self.freq = len(doc)

    def add_document(self, doc):
        self.documents.append(doc)
        self.freq += len(doc)
