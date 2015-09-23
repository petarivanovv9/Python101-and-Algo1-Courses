class Node:

    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.previous = None

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def set_previous(self, node):
        self.previous = node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class BuildScript:

    @staticmethod
    def build_script(projects, wanted_project, dependencies):
        data = BuildScript.make_graph(projects, dependencies, wanted_project)

        if not data:
            return "BUILD ERROR"

        graph = data[0]
        wanted_project_node = data[1]
        return BuildScript.go_down(graph, wanted_project_node)

    @staticmethod
    def go_down(graph, wanted_project_node):
        starting_point = wanted_project_node
        # checked = []
        stack = [starting_point]
        leaves = []

        while len(stack) != 0:
            current_node = stack.pop(0)
            for node in current_node.neighbours:
                if node not in stack:
                    stack.append(node)

            if len(current_node.neighbours) == 0 or BuildScript.check_if_subset(leaves, current_node.neighbours):
                if current_node not in leaves:
                    leaves.append(current_node)
            else:
                stack.append(current_node)

        return leaves

    @staticmethod
    def make_graph(projects, dependencies, wanted_project):
        nodes = []
        for project in projects:
            nodes.append(Node(project))
            if project == wanted_project:
                wanted_project_node = nodes[-1]

        for i in range(len(dependencies)):
            for j in range(1, len(dependencies[i])):
                index_node = projects.index(dependencies[i][j])

                if nodes[i] in nodes[index_node].neighbours or nodes[i].value == nodes[index_node].value:
                    return False
                nodes[i].add_neighbour(nodes[index_node])
                nodes[index_node]

        return [nodes, wanted_project_node]

    @staticmethod
    def check_if_subset(bigset, smallset):
        for el in smallset:
            if el not in bigset:
                return False

        return True


def main():

    number_of_projects = int(input())

    projects = input()
    p = [x for x in projects.split()]

    # print(p)

    wanted_project = input()

    dependencies = []

    while number_of_projects != 0:
        number_of_projects -= 1

        bam = input()
        temp = [x for x in bam.split()]
        temp[0] = int(temp[0])
        # print(temp)

        dependencies.append(temp)
        temp = []

    # print(dependencies)

    print(BuildScript.build_script(p, wanted_project, dependencies))

if __name__ == '__main__':
    main()
