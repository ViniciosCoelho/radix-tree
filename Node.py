class Node:
    def __init__(self, word = None):
        self.edges = []
        self.word = word

    def is_leaf(self):
        return False if len(self.edges) else True
    
    def add_edge(self, edge):
        self.edges.append(edge)