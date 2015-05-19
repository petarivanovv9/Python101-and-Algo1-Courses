class Histogram:

    def __init__(self):
        self.dict = {}

    def add(self, server):
        if server in self.dict.keys():
            self.dict[server] += 1
        else:
            self.dict[server] = 1

    def count(self, server):
        return self.dict[server]

    def get_dict(self):
        return self.dict
