from directed_graph import DirectedGraph


class GithubNetwork:

    def __init__(self):
        self.graph = DirectedGraph()
        self.person = None

    def build_network_for(self, person, level):
        current_level = 0
        self.person = person
        visited = set()
        queue = []
        queue.append((current_level, person))
        visited.add(person)

        while len(queue) != 0:
            current_level, current_user = queue.pop(0)

            if current_level + 1 > level:
                break

            if len(current_user.get_followers()) == 0:
                current_user.make_followers()
            followers = current_user.get_followers()

            print ("BAAAAAA")

            for user in followers:
                if user not in visited:
                    queue.append((current_level + 1, user))
                    visited.add(user)
                    self.graph.add_edge(current_user, user)
                    print ("DEAAAAAM")

        print ("HEREEEE")

        current_level = 0
        visited = set()
        queue = []
        queue.append((current_level, person))
        visited.add(person)

        while len(queue) != 0:
            current_level, current_user = queue.pop(0)

            if current_level + 1 > level:
                break

            if len(current_user.get_following()) == 0:
                current_user.make_following()
            following = current_user.get_following()

            for user in following:
                if user not in visited:
                    queue.append((current_level + 1, user))
                    visited.add(user)
                    self.graph.add_edge(user, current_user)

    def do_you_follow(self, user):
        return self.graph.edge_between(self.person, user)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.person, user)

    def does_he_she_follows(self, user):
        return self.graph.edge_between(user, self.person)

    def does_he_she_follows_indirectly(self, user):
        return self.graph.edge_between(self.person, user)

    def who_follows_you_back(self):
        followers = self.person.get_followers()
        following = self.person.get_following()
        following_back = []

        for user in followers:
            if user in following:
                following_back.append(user)

        return following_back
