class Positions:

    def __init__(self, doc, pos):
        self.doc = doc
        self.position_list = [pos]

    def add(self, pos):
        self.position_list.append(pos)

    def __len__(self):
        return len(self.position_list)

    def __lt__(self, other):
        return self.doc < other.doc
