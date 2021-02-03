import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = (None, sys.maxsize)
        self.FRONT = 1

    def parent(self, pos):

        return pos // 2

    def leftChild(self, pos):

        return 2 * pos

    def rightChild(self, pos):

        return (2 * pos) + 1

    def isLeaf(self, pos):

        if (self.size // 2) < pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def max_heapify(self, pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos][1] < self.Heap[self.leftChild(pos)][1] or
                    self.rightChild(pos) <= self.size and self.Heap[pos][1] < self.Heap[self.rightChild(pos)][1]):

                if (self.Heap[self.leftChild(pos)][1] >
                        self.Heap[self.rightChild(pos)][1]):
                    self.swap(pos, self.leftChild(pos))
                    self.max_heapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.max_heapify(self.rightChild(pos))

    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current][1] >
               self.Heap[self.parent(current)][1]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extract_max(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        if self.size > 0:
            self.max_heapify(self.FRONT)

        return popped

    def select_top(self, results, top):
        for res in results:
            self.insert(res)
        top_results = []
        for i in range(top):
            if self.size == 0:
                break
            top_results.append(self.extract_max())
        return top_results
