from github_network import GithubNetwork
from github_person import GithubPerson


GITHUB_API = "https://api.github.com/users/"
CLIENT_ID = ....
CLEINT_SECRET = ....


def main():
    petar = GithubPerson(GITHUB_API + "pepincho" + CLIENT_ID + CLEINT_SECRET)
    desislava = GithubPerson(GITHUB_API + "6desislava6" + CLIENT_ID + CLEINT_SECRET)
    nikola = GithubPerson(GITHUB_API + "Rage2Play" + CLIENT_ID + CLEINT_SECRET)

    network = GithubNetwork()
    network.build_network_for(petar, 2)

    print ("Do I follow?")
    print (network.do_you_follow(desislava))

    print ("Does she follow me?")
    print (network.does_he_she_follows(desislava))

    print ("Who follows me back?")
    print (network.who_follows_you_back())

    print ("Do I follow Nikola?")
    print (network.do_you_follow_indirectly(nikola))


if __name__ == '__main__':
    main()
