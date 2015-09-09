# key - name
# value - number

# Binary Search Tree


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = Tree.insert_impl(self.root, key, value)

    @staticmethod
    def insert_impl(subtree_root, key, value):
        if subtree_root is None:
            return Node(key, value)
        if subtree_root.key == key:
            subtree_root.value = value
            return subtree_root

        if key < subtree_root.key:
            subtree_root.left = Tree.insert_impl(subtree_root.left, key, value)
        else:
            subtree_root.right = Tree.insert_impl(subtree_root.right, key, value)

        return subtree_root

    def find(self, key):
        return Tree.find_impl(self.root, key)

    @staticmethod
    def find_impl(subtree_root, key):
        if subtree_root is None:
            return None
        if subtree_root.key == key:
            return subtree_root.value
        if subtree_root.key > key:
            return Tree.find_impl(subtree_root.left, key)
        else:
            return Tree.find_impl(subtree_root.right, key)

    def list(self):
        result = []
        Tree.list_impl(self.root, result)

        return result

    @staticmethod
    def list_impl(subtree_root, result):
        if subtree_root is None:
            return

        Tree.list_impl(subtree_root.left, result)

        result.append((subtree_root.key, subtree_root.value))

        Tree.list_impl(subtree_root.right, result)

    def remove(self, name):
        self.root = Tree.remove_impl(self.root, name)

    @staticmethod
    def remove_impl(subtree_root, name):
        if subtree_root is None:
            return None

        if subtree_root.key == name:
            if subtree_root.right is None:
                subtree_root = subtree_root.left
            else:
                smallest, new_right = Tree.remove_smallest(subtree_root.right)
                subtree_root.key = smallest.key
                subtree_root.value = smallest.value
                subtree_root.right = new_right

        else:
            if name > subtree_root.key:
                subtree_root.right = Tree.remove_impl(subtree_root.right, name)
            else:
                subtree_root.left = Tree.remove_impl(subtree_root.left, name)

        return subtree_root

    @staticmethod
    def remove_smallest(subtree_root):
        if subtree_root.left is None:
            return (subtree_root, subtree_root.right)
        else:
            smallest, new_left = Tree.remove_smallest(subtree_root.left)
            subtree_root.left = new_left
            return (smallest, subtree_root)


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class PhoneBook:

    def __init__(self):
        self.data = Tree()

    # inserts a new contact
    def insert(self, number, name):
        self.data.insert(name, number)

    # lookup a name and print its phone number
    def lookup(self, name):
        result = self.data.find(name)
        if result is None:
            return 'NOT FOUND!'
        else:
            return result

    # list all records in an alphabetical order
    def list(self):
        return self.data.list()

    # remove a record for a given name
    def remove(self, name):
        self.data.remove(name)


def main():

    a = PhoneBook()
    N = int(input())

    while N != 0:
        c = input()
        command = c.split()

        if command[0] == 'insert':
            a.insert(command[1], command[2])
        elif command[0] == 'lookup':
            print(a.lookup(command[1]))
        elif command[0] == 'list':
            contacts = a.list()
            for contact in contacts:
                print(contact[0] + ' ' + contact[1])
        elif command[0] == 'remove':
            a.remove(command[1])
        else:
            pass

        N -= 1


if __name__ == '__main__':
    main()
