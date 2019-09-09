from Node import Node

class RadixTree:
    def __init__(self):
        self.root = Node()

    def __find_word_nearest_node(self, word: str):
        node = self.root
        found_word = ''
        found_next_word = True
        parent_node = None

        while not node.is_leaf() and found_next_word:
            found_next_word = False

            for edge in node.edges:
                current_word = edge.word

                if word.startswith(current_word) and current_word != '' or word == '' and current_word == '':
                    word = word.replace(current_word, '', 1)
                    found_word += current_word
                    found_next_word = True
                    parent_node = node
                    node = edge
                    break
        
        return found_word, node, parent_node
    
    def find(self, word: str):
        word_found, node, _ = self.__find_word_nearest_node(word)

        if word == word_found and node.is_leaf():
            return True
        else:
            return False

        return is_word_found
    
    def insert(self, word: str):
        word_found, node, _ = self.__find_word_nearest_node(word)

        is_leaf = node.is_leaf()

        if word_found == word and is_leaf:
            return False

        if is_leaf:
            difference_index = 0
            current_word = word_found
            current_similar_index = 0

            if len(word) > len(current_word):
                if word[:-1] == current_word:
                    difference_index = len(current_word)
                    most_similar_word = current_word
            elif len(word) < len(current_word):
                if word == current_word[:-1]:
                    difference_index = len(word)
                    most_similar_word = current_word
            
            if difference_index == 0:
                suffix = word[len(word_found):]
                new_node = Node(suffix)
                node.add_edge(new_node)
            else:
                prefix = word[len(word_found):]
                prefix = prefix[:difference_index]
                prefix_size = len(word_found)

                suffix1 = most_similar_word[prefix_size:]
                suffix2 = word[prefix_size:]

                new_node1 = Node(suffix1)
                new_node1.edges = node.edges
                node.edges = []

                new_node2 = Node(suffix2)

                node.word = prefix
                node.add_edge(new_node1)
                node.add_edge(new_node2)
        else:
            difference_index = 0
            most_similar_node = None
            most_similar_word = None

            for edge in node.edges:
                current_word = word_found + edge.word
                current_similar_index = 0

                if len(word) > len(current_word):
                    if word[:-1] == current_word:
                        if word[-1] == word[-2]:
                            difference_index = 0
                            most_similar_node = None
                            most_similar_word = None
                            continue

                        difference_index = len(current_word)
                        most_similar_node = edge
                        most_similar_word = current_word
                        continue
                    elif word.startswith(current_word):
                        difference_index = len(current_word)
                        most_similar_node = edge
                        most_similar_word = current_word
                        continue
                elif len(word) < len(current_word):
                    if word == current_word[:-1]:
                        if current_word[-1] == current_word[-2]:
                            difference_index = 0
                            most_similar_node = None
                            most_similar_word = None
                            continue

                        difference_index = len(word)
                        most_similar_node = edge
                        most_similar_word = current_word
                        continue
                    elif current_word.startswith(word):
                        difference_index = len(word)
                        most_similar_node = edge
                        most_similar_word = current_word
                        continue

                for x, y in zip(word, current_word):
                    if x != y:
                        if current_similar_index > difference_index:
                            difference_index = current_similar_index
                            most_similar_node = edge
                            most_similar_word = current_word
                        break
                    current_similar_index += 1
                
            if difference_index == 0:
                suffix = word[len(word_found):]
                new_node = Node(suffix)
                node.add_edge(new_node)
            else:
                prefix = word[len(word_found):]
                prefix = prefix[:difference_index]
                prefix_size = len(word_found) + len(prefix)

                suffix1 = most_similar_word[prefix_size:]
                suffix2 = word[prefix_size:]

                new_node1 = Node(suffix1)
                new_node1.edges = most_similar_node.edges
                most_similar_node.edges = []

                new_node2 = Node(suffix2)

                most_similar_node.word = prefix
                most_similar_node.add_edge(new_node1)
                most_similar_node.add_edge(new_node2)

        return True

    def remove(self, word: str):
        word_found, node, parent_node = self.__find_word_nearest_node(word)

        if not node.is_leaf() or word != word_found:
            return False

        parent_node.edges.remove(node)
        
        if len(parent_node.edges) == 1:
            child_node = parent_node.edges.pop()
            parent_node.word += child_node.word
            parent_node.edges = child_node.edges
        
        return True
    
    def print(self):
        self.root.print()