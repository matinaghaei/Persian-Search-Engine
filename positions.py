class Positions:
    sort_by_id = True

    def __init__(self, doc, pos):
        self.doc_id = doc
        self.position_list = [pos]

    def add(self, pos):
        self.position_list.append(pos)

    def get_size(self):
        return len(self.position_list)

    def __lt__(self, other):
        if self.sort_by_id:
            return self.doc_id < other.doc_id
        return self.get_size() < other.get_size()
