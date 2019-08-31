# from typing import Tuple
from Node import Node

class RadixTree:
    def __init__(self):
        self.root = Node()
        self.node_counter = 0

    def __find_word_nearest_node(self, word: str):
        node = self.root

        while not node.is_leaf():
            current_word = word

            for edge in node.edges:
                current_word = edge.word

                if word.startswith(current_word):
                    word.replace(current_word, '')
                    node = edge
            
            if current_word == word:
                return False, node

        if word == node.word:
            return True, node
        else:
            return False, node
    
    def find(self, word: str):
        found_word, node = self.__find_word_nearest_node(word)
        return found_word
    
    def insert(self, word):
        found_word, node = self.__find_word_nearest_node(word)

        if found_word:
            return False
        if