# Priority Queue

import heapq


class Packet:
    PROTOCOL_PRIORITY = {
        'ICMP': 10,
        'UDP': 9,
        'RTM': 8,
        'IGMP': 7,
        'DNS': 6,
        'TCP': 5
    }

    def __init__(self, protocol, payload, sequence_number):
        self.priority = Packet.PROTOCOL_PRIORITY[protocol]
        self.payload = payload
        self.sequence_number = sequence_number

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.sequence_number < other.sequence_number
        else:
            return self.priority > other.priority


class BandwidthManager:

    def __init__(self):
        self.heap = []
        self.sequence_number = 0

    # receives a packet with specified protocol and payload
    def rcv(self, protocol, payload):
        new_packet = Packet(protocol, payload, self.sequence_number)
        heapq.heappush(self.heap, new_packet)
        self.sequence_number += 1

    # returns the payload of the packet which should be sent
    def send(self):
        if len(self.heap) == 0:
            return 'Nothing to send!'

        return heapq.heappop(self.heap).payload


def main():
    N = int(input())
    bm = BandwidthManager()

    while N != 0:
        line = input().split()
        if line[0] == 'rcv':
            bm.rcv(line[1], line[2])
        else:
            print(bm.send())

        N -= 1


if __name__ == '__main__':
    main()
