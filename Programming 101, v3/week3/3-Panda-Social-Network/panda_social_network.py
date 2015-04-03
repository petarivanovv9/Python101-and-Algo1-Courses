from panda import Panda


class PandaAlreadyThere(Exception):
    pass


class PandaAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.network_dict = {}

    def add_panda(self, panda):
        if panda in self.network_dict.keys():
            raise PandaAlreadyThere
        self.network_dict[panda] = []

    def has_panda(self, panda):
        return panda in self.network_dict.keys()

    def make_friends(self, panda1, panda2):
        if (panda2 in self.network_dict.keys() and panda1 in self.network_dict[panda2]):
            raise PandaAlreadyFriends

        if self.has_panda(panda1) is True:
            self.network_dict[panda1] += [panda2]
        else:
            self.network_dict[panda1] = [panda2]

        if self.has_panda(panda2) is True:
            self.network_dict[panda2] += [panda1]
        else:
            self.network_dict[panda2] = [panda1]

    def are_friends(self, panda1, panda2):
        if panda1 in self.network_dict[panda2]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if panda not in self.network_dict.keys():
            return False
        else:
            return self.network_dict[panda]

    def connection_level(self, panda1, panda2):
        start = panda1
        end = panda2

        result = find_shortest_path(self.network_dict, start, end, path=[])

        if result == None:
            return 0

        return len(result) - 1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != 0

    def how_many_gender_in_network(self, level, panda, gender):
        gender_counter = 0

        for next_panda in self.network_dict.keys():
             if next_panda != panda:
                if self.connection_level(panda, next_panda) == level and next_panda.get_gender() == gender:
                    gender_counter += 1

        return gender_counter


def find_all_paths(graph, start, end, path=[]):
    path += [start]

    if start == end:
        return [path]
    if start not in graph.keys():
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph.keys():
        return None

    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest
