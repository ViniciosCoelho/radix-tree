from Node import Node
from RadixTree import RadixTree

if __name__ == "__main__":
    tree = RadixTree()

    print('Inserting...')
    print(tree.insert('Potatoe'))
    print(tree.insert('Potatao'))
    print(tree.insert('Potata'))
    print(tree.insert('Potataa'))
    print(tree.insert('Potataaa'))

    print('Finding...')
    print(tree.find('Potatoe'))
    print(tree.find('Potatao'))
    print(tree.find('Potata'))
    print(tree.find('Potataa'))
    print(tree.find('Potataaa'))
    print(tree.find('Potataaaa'))
    print(tree.find('Miojo'))

    print('Removing...')
    print(tree.remove('Potatoe'))
    print(tree.remove('Asloc'))
    print(tree.remove('Potata'))

    print('Finding again...')
    print(tree.find('Potatoe'))
    print(tree.find('Potata'))

    print('Showing Radix Tree:')
    tree.print()