class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next

    def __repr__(self):
        return str(self.value)


class KLists:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, value):
        node = Node(value)

        if self.first is None:
            self.first = node
            self.size += 1
            self.last = node

            return

        self.size += 1
        self.last.next = node
        self.last = node

    def remove_first(self):
        removed = self.first
        self.first = self.first.next
        self.size -= 1

        return removed

    def __repr__(self):
        result = ""
        next_str = " "

        node = self.first

        while node is not None:
            if node != self.first:
                result += next_str
            result += str(node.value)
            node = node.next

        return result

    # Merge K sorted lists.
    # lists - [Node]
    @staticmethod
    def merge(lists):
        total_size = 0

        for k_list in lists:
            total_size += k_list.size

        result_list = KLists()

        while result_list.size < total_size:
            lowest = None

            for k_list in lists:
                if k_list.size > 0:
                    if lowest is None:
                        lowest = k_list
                    elif k_list.first.value <= lowest.first.value:
                        lowest = k_list

            result_list.add(lowest.first)
            lowest.remove_first()

        return result_list


def main():

    k1 = sorted([88, 56, 10, 16, 91, 60])
    k2 = sorted([74, 75, 10, 30])
    k3 = sorted([93, 18, 19, 55, 82, 13])

    lists = [k1, k2, k3]
    k_lists = []

    for item in lists:
        k_list = KLists()
        for num in item:
            k_list.add(num)
        k_lists.append(k_list)

    for k_list in k_lists:
        print(k_list)

    result = KLists.merge(k_lists)
    print(result)


if __name__ == '__main__':
    main()
