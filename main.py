from Node import Node
from RadixTree import RadixTree

if __name__ == "__main__":
    tree = RadixTree()

    op = ''

    print(tree.insert('Potatoe'))
    print(tree.insert('Potatao'))
    print(tree.insert('Potata'))
    print(tree.insert('Potataa'))
    print(tree.insert('Potataaa'))

    tree.insert('Batata')
    tree.insert('a')
    tree.insert('Batat')

    while op != '4':
        tree.print()

        print()
        print('1 - Insert word')
        print('2 - Find word')
        print('3 - Delete word')
        print('4 - Exit')
        op = input('Choose an option: ')

        if op == '1':
            word = input('Type a word: ')
            tree.insert(word)
            print()
        elif op == '2':
            word = input('Type a word: ')
            print('Found word = ' + str(tree.find(word)) + '\n')
        elif op == '3':
            word = input('Type a word: ')
            print('Removed word = ' + str(tree.remove(word)) + '\n')
        elif op == '4':
            print('Exiting...')
        else:
            print('Wrong option...\n')