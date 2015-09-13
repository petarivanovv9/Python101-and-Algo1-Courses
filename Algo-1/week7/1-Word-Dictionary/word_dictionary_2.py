class Node:

    def __init__(self):
        self.ends_word = False
        self.children = dict()

    def __repr__(self):
        return str(self.children)

    def __str__(self):
        return str(self.children)


class WordDict:

    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = Node()
            curr_node = self.root

            for letter in word:
                curr_node.children[letter] = Node()
                curr_node = curr_node.children[letter]

            curr_node.ends_word = True

            return

        curr_node = self.root

        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                curr_node.children[letter] = Node()
                curr_node = curr_node.children[letter]

        curr_node.ends_word = True

        return

    def contains(self, word):
        curr_node = self.root

        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                return False

        if curr_node.ends_word:
            return True
        else:
            return False

    def __str__(self):
        return str(self.root)


def main():

    w = WordDict()

    num = int(input())
    res = list()
    for i in range(num):
        j = input()
        if j.split()[0] == 'insert':
            w.insert(j.split()[1])
        elif j.split()[0] == 'contains':
            if w.contains(j.split()[1]) is False:
                res.append("false")
            else:
                res.append("true")
                # res.append(w.contains(j.split()[1]))

    for r in res:
        print(r)


if __name__ == '__main__':
    main()
