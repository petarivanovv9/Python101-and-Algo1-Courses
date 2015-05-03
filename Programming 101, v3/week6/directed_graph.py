class AlreadyThere(Exception):
    pass


class CantFollowYourself(Exception):
    pass


class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node in self.nodes.keys():
            raise AlreadyThere
        self.nodes.update({node: set()})

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes.keys():
            self.add_node(node_a)
        if node_b not in self.nodes.keys():
            self.add_node(node_b)
        if node_a == node_b:
            raise CantFollowYourself
        self.nodes[node_a].add(node_b)

    def get_neighbours_for(self, node):
        return self.nodes[node]

    def path_between(self, node_a, node_b):
        return self.are_connected(node_a, node_b, self.nodes)

    def edge_between(self, node_a, node_b):
        return node_b in self.nodes[node_a]

    @staticmethod
    def are_connected(start, end, graph):
        visited = set()
        queue = []
        path_to = {}
        queue.append(start)
        visited.add(start)
        path_to[start] = None
        found = False

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == end:
                found = True
                return found

            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False
