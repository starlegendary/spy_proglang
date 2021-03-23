class Node:
    def __init__(self, curr=None, prev=None, futu = None):
        if futu is None:  self.futu = []
        self.curr = curr
        self.futu = futu
        self.prev = prev
class Tree:
    def __init__(self, dick = {}):
        self.dick = dick
        self.root = Node()

