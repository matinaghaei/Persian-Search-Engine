class Doc:

    def __init__(self, doc_id, text):
        self.id = doc_id
        self.text = text
        self.tf_idf_vector = {}

    def add_tf_idf(self, term, tf_idf):
        self.tf_idf_vector[term] = tf_idf

    def get_vector_length(self):
        length = 0
        for val in self.tf_idf_vector.values():
            length += val * val
        return length
