from doc import Doc


class Documents:

    def __init__(self):
        self.docs = {}

    def add(self, doc_id, text):
        self.docs[doc_id] = Doc(doc_id, text)

    def get_doc(self, doc_id):
        return self.docs[doc_id]

    def get_docs(self):
        return self.docs.values()

    def get_size(self):
        return len(self.docs)

    def calculate_center(self):
        super_vector = {}
        for doc in self.docs:
            for k, v in doc.tf_idf_vector.items():
                super_vector.setdefault(k, []).append(v)
        center_vector = {}
        for k, v in super_vector.items():
            center_vector[k] = sum(v) / len(v)
        return center_vector
