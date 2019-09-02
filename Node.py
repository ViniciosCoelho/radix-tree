class Node:
    def __init__(self, word = None):
        self.edges = []
        self.word = word

    def is_leaf(self):
        return False if len(self.edges) else True
    
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def print(self, indent=""):
        if self.word is None:
            printed_word = '*Root*'
        elif self.word == '':
            printed_word = '.'
        else:
            printed_word = self.word

        print(indent + printed_word + '(')

        for edge in self.edges:
            edge.print(indent + '   ')
        
        print(indent + ')')