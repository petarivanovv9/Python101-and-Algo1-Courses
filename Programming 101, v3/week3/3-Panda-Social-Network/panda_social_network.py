from panda import Panda
import json


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

        if result is None:
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

    def get_friends_of_panda(self, panda):
        return [panda.get_name() for panda in self.network_dict[panda]]

    def save_to_file(self):
        members = {}
        for member in self.network_dict.keys():
            members[member.get_name()] = member.__dict__

        with open('panda_network_members.txt', 'w') as outfile:
            outfile.write(json.dumps(members))

        friends = {}
        for current_panda in self.network_dict.keys():
            friends[current_panda.get_name()] = self.get_friends_of_panda(current_panda)

        with open('panda_network_friends.txt', 'w') as outfile:
            outfile.write(json.dumps(friends))

    def load_from_file(self):
        members = {}
        with open('panda_network_members.txt', 'r') as infile:
            members = json.load(infile)

        for panda in members.keys():
            self.add_panda(Panda(members[panda]['name'], members[panda]['email'], members[panda]['gender']))

        friends = {}
        with open('panda_network_friends.txt', 'r') as infile:
            friends = json.load(infile)

        for panda in friends.keys():
            for friend_panda in friends[panda]:
                some_panda = Panda(members[panda]['name'], members[panda]['email'], members[panda]['gender'])
                some_panda_friend = Panda(members[friend_panda]['name'], members[friend_panda]['email'], members[friend_panda]['gender'])
                if self.are_friends(some_panda, some_panda_friend) is False:
                    self.make_friends(some_panda, some_panda_friend)


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


network = PandaSocialNetwork()

ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
mimi = Panda('Mimi', 'mimi@mail.bg', 'female')
gosho = Panda('Gosho', 'gosho@mail.bg', 'male')
pesho = Panda('Pesho', 'pesho@mail.bg', 'male')

network.add_panda(pesho)

network.make_friends(ivo, rado)
network.make_friends(ivo, gosho)
network.make_friends(ivo, mimi)
network.make_friends(rado, mimi)

network.save_to_file()

# network.load_from_file()

print (network.network_dict)
