class PostingsList:

    def __init__(self, token, doc):
        self.token = token
        self.documents = [doc]
        self.champion_list = []
        self.freq = doc.get_size()

    def add_document(self, doc):
        self.documents.append(doc)
        self.freq += doc.get_size()

    def get_doc_freq(self):
        return len(self.documents)

    def add_to_champion(self, docs):
        self.champion_list.extend(docs)
