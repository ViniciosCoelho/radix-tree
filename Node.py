from sys import stdout

class Node:
    def __init__(self, word = None):
        self.edges = []
        self.word = word

    def is_leaf(self):
        return False if len(self.edges) else True
    
    def add_edge(self, edge):
        self.edges.append(edge)

    def print(self, indent="", last=True, stack=""):
        if indent != "":
            stack = stack + self.word

        stdout.write(indent)

        if last:
            stdout.write("┗╾ ")
            indent += "  "
        else:
            stdout.write("┣╾ ")
            indent += "┃ "

        if self.word is None:
            stdout.write("{}".format('*ROOT*'))
        elif self.word == '':
            stdout.write("{}".format('*'))
        else:
            stdout.write("{}".format(self.word))

        print(" - {}".format(stack))

        for i, edge in enumerate(self.edges):
            edge.print(indent, i == len(self.edges) - 1, stack)