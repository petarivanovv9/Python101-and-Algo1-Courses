# Birthday ranges 2 implemented with Indexed Tree


class IndexedTree:
    VALUES_LEVEL = 9

    def __init__(self):
        self.values = [0] * 1024

    @staticmethod
    def find_position(index, level=VALUES_LEVEL):
        return 2 ** level + index - 1

    def add(self, index, value):
        position = IndexedTree.find_position(index)

        while True:
            self.values[position] += value
            parent = (position - 1) // 2

            if position == 0:
                break
            else:
                position = parent

    def remove(self, index, value):
        position = IndexedTree.find_position(index)

        if self.value[position] - value <= 0:
            value = self.values[position]
        self.add(index, -value)

    def count_from_beginning(self, end):
        counter = 0
        level = IndexedTree.VALUES_LEVEL

        while end >= 0:
            position = IndexedTree.find_position(end, level)

            if end % 2 == 0:
                counter += self.values[position]
                end -= 1
            else:
                end //= 2
                level -= 1

        return counter

    def count(self, start_day, end_day):
        b = self.count_from_beginning(end_day)
        a = self.count_from_beginning(start_day - 1)
        return b - a


def main():
    row = input().split()
    N = int(row[0])
    M = int(row[1])
    bd = input().split()
    tree = IndexedTree()
    for date in bd:
        tree.add(int(date), 1)
    while M != 0:
        command = input().split()
        M -= 1
        if command[0] == 'count':
            print(tree.count(int(command[1]), int(command[2])))
        elif command[0] == 'add':
            tree.add(int(command[1]), int(command[2]))
        else:
            tree.remove(int(command[1]), int(command[2]))


if __name__ == '__main__':
    main()
