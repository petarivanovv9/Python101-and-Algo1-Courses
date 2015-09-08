class BST:

    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def add_left(self, left):
            self.left = left

        def add_right(self, right):
            self.right = right

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_value(self):
            return self.value

    # Checks if a binary tree is a binary search tree.
    # root - node with `left`, `right` and `value` properties
    @staticmethod
    def isBST(root):
        left_node = root.left
        right_node = root.right

        if left_node is not None:
            if left_node.value > root.value:
                return False
            BST.isBST(left_node)

        if right_node is not None:
            if right_node.value < root.value:
                return False
            BST.isBST(right_node)

        return True


def main():
    node1 = BST.Node(19)
    node2 = BST.Node(12)
    # node3 = BST.Node(12)
    node3 = BST.Node(25)
    node4 = BST.Node(4)
    node5 = BST.Node(17)
    node6 = BST.Node(22)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    print(BST.isBST(node1))


if __name__ == '__main__':
    main()
