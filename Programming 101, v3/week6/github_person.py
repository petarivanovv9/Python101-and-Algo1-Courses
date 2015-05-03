import requests


class GithubPerson:

    GITHUB_API = "https://api.github.com/users/"
    CLIENT_ID = "?client_id=f5ec483b648f040cdd57"
    CLEINT_SECRET = "&client_secret=0d67a9185b976c353022c1b245f20e3326a6e4d2"

    def __init__(self, person_info_url):
        person_info = requests.get(person_info_url).json()

        self.login = person_info["login"]
        self.url = person_info["url"]
        self.following_url = GITHUB_API + self.login + CLIENT_ID + CLEINT_SECRET + "/following"
        self.followers_url = GITHUB_API + self.login + CLIENT_ID + CLEINT_SECRET + "/followers"
        self.followers_json = requests.get(self.followers_url).json()
        self.following_json = requests.get(self.following_url).json()
        self.followers = []
        self.following = []

    def __hash__(self):
        return hash(self.url)

    def __repr__(self):
        return str(self.login)

    def __str__(self):
        return str(self.login)

    def __eq__(self, other):
        return self.login == other.login

    def make_followers(self):
        for follower in self.followers_json:
            current_url = GithubPerson.GITHUB_API + follower["login"] + GithubPerson.CLIENT_ID + GithubPerson.CLEINT_SECRET
            current_person = GithubPerson(current_url)
            self.followers.append(current_person)

    def make_following(self):
        for following in self.following_json:
            current_url = GithubPerson.GITHUB_API + following["login"] + GithubPerson.CLIENT_ID + GithubPerson.CLEINT_SECRET
            current_person = GithubPerson(current_url)
            self.following.append(current_person)

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following
