class MinMaxHeap:

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

    # Checks if a binary tree is a min/max heap.
    # root - node with `left`, `right` and `value` properties
    def isMinMax(self, root):
        return self.is_min_max_level(root, 1)

    @staticmethod
    def check_children(root):
        if root.left is None:
            return root.right.value > root.value
        if root.right is None:
            return root.left.value > root.value

        left_bigger = root.left is None or root.left.value > root.value
        right_bigger = root.right is None or root.right.value > root.value

        # If both are bigger or if both are less
        return left_bigger == right_bigger

    @staticmethod
    def check_if_children_bigger(root):
        if root.left is None:
            return root.right.value > root.value
        if root.right is None:
            return root.left.value > root.value

        return root.left.value > root.value and root.right.value > root.value

    @staticmethod
    def is_min_max_level(root, level):

        if root.left is None and root.right is None:
            return True

        if not MinMaxHeap.check_children(root):
            return False

        isEven = level % 2 == 0

        # If it's even -> check_if_children... must be True
        # So isEven must be the same as check_if...
        if MinMaxHeap.check_if_children_bigger(root) == isEven:
            return False

        if root.left is not None:
            return MinMaxHeap.is_min_max_level(root.left, level + 1)
        if root.right is not None:
            return MinMaxHeap.is_min_max_level(root.right, level + 1)

        return True


def main():

    heap = MinMaxHeap()

    node1 = MinMaxHeap.Node(8)
    node2 = MinMaxHeap.Node(60)
    node3 = MinMaxHeap.Node(41)
    node4 = MinMaxHeap.Node(60)
    # node4 = MinMaxHeap.Node(61)
    node5 = MinMaxHeap.Node(10)
    node6 = MinMaxHeap.Node(11)

    node7 = MinMaxHeap.Node(88)
    node8 = MinMaxHeap.Node(10)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    node4.left = node7
    node5.right = node8

    print(heap.isMinMax(node1))


if __name__ == '__main__':
    main()
