class WordDictionary:

    class Node:

        def __init__(self, char):
            # char is a substring of the phone number
            self.char = char
            # 10 digits
            self.children_nodes = [None for i in range(26)]
            self.isTerminal = False

        def get_char(self):
            return self.char

        def add_node(self, node):
            index = ord(node.char[0]) - 97
            self.children_nodes[index] = node

        def get_node(self, char):
            index = ord(char) - 97
            return self.children_nodes[index]

        def __repr__(self):
            return self.char

    def insert(self, string):
        current_node = self.root

        for index in range(len(string)):
            char = string[index]
            result_node = current_node.get_node(char)

            if result_node is None:
                new_node = WordDictionary.Node(string[index:])
                if index == len(string) - 1:
                    new_node.isTerminal = True

                current_node.add_node(new_node)
                current_node = new_node
            else:
                current_node = result_node
        return self.root

    def contains(self, phone_number):
        root = self.root
        index = 1
        phone_number = str(phone_number)
        current_node = root.get_node(phone_number[index - 1])
        while current_node is not None and index < len(phone_number):
            current_node = current_node.get_node(phone_number[index])
            index += 1
            # print(current_node)
        if current_node is not None:
            return True
        return False

    def __init__(self):
        self.root = WordDictionary.Node('')


def main():
    w = WordDictionary()
    # w.insert('alabala')
    # w.insert('asdf')
    # print(w.contains('alabala'))
    # w.insert('aladin')
    # print(w.contains('asdf'))
    # print(w.contains('aladin'))
    # w.insert('circle')
    # print(w.contains('rectangle'))
    # print(w.contains('square'))

    N = int(input())

    while N != 0:
        c = input()
        command = c.split()

        if command[0] == 'insert':
            w.insert(command[1])
        elif command[0] == 'contains':
            print(w.contains(command[1]))
        else:
            pass

        N -= 1


if __name__ == '__main__':
    main()
