# from typing import Tuple
from Node import Node

class RadixTree:
    def __init__(self):
        self.root = Node()
        self.node_counter = 0

    def __find_word_nearest_node(self, word: str):
        node = self.root
        found_word = ''

        while not node.is_leaf():
            current_word = word

            for edge in node.edges:
                current_word = edge.word

                if word.startswith(current_word):
                    word.replace(current_word, '')
                    found_word += current_word
                    node = edge
            
            if current_word == word:
                break
        
        return found_word, node
    
    def find(self, word: str):
        word_found, node = self.__find_word_nearest_node(word)

        if word == word_found:
            return True
        else:
            return False

        return is_word_found
    
    def insert(self, word: str):
        word_found, node = self.__find_word_nearest_node(word)

        if word_found == word:
            return False

        if node.is_leaf():
            split_index = node.word.find(word)
            preffix = word.
        
        return True