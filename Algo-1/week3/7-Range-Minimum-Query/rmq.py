import math


class RMQ:

    MAX_VALUE = 2 ** 31

    def __init__(self, size):
        self.level = RMQ.determine_level(size)
        self.values = [RMQ.MAX_VALUE] * (2 ** (self.level + 1))

    @staticmethod
    def determine_level(elements_count):
        a = 1
        level = 0

        while a < elements_count:
            a *= 2
            level += 1

        return level

    @staticmethod
    def find_position(index, level):
        return 2 ** level + index - 1

    # sets the value at index
    def set(self, index, value):
        position = RMQ.find_position(index, self.level)

        self.values[position] = value
        position = (position - 1) // 2

        while True:
            self.values[position] = min(self.values[2 * position + 1], self.values[2 * position + 2])
            parent = (position - 1) // 2
            if position == 0:
                break
            else:
                position = parent

    # returns the minimum value in a range
    def minimum(self, start_index, end_index):
        level = self.level
        result = self.values[RMQ.find_position(start_index, level)]

        while start_index <= end_index:
            result = min(result, self.values[RMQ.find_position(start_index, level)], self.values[RMQ.find_position(end_index, level)])

            if end_index % 2 == 0:
                end_index = (end_index // 2) - 1
            else:
                end_index //= 2

            if start_index % 2 == 0:
                start_index //= 2
            else:
                start_index = (start_index // 2) + 1

            level -= 1

        return result


def main():
    line = input().split()
    N = int(line[0])
    K = int(line[1])

    values = input().split()
    rmq = RMQ(N)

    for index in range(len(values)):
        rmq.set(index, int(values[index]))

    while K != 0:
        command = input().split()
        if command[0] == 'set':
            rmq.set(int(command[1]), int(command[2]))
        else:
            print(rmq.minimum(int(command[1]), int(command[2])))
        K -= 1


if __name__ == '__main__':
    main()
