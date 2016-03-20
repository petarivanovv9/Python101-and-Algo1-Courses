import re


class WrongEmailError(Exception):
    pass


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        if validate_email(email) == False:
            raise WrongEmailError
        self.email = email
        self.gender = gender

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and self.gender == other.gender

    def __hash__(self):
        return hash(self.email)

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def is_male(self):
        return self.gender == "male"

    def is_female(self):
        return self.gender == "female"

    def __str__(self):
        return "My panda with name {} is with email {} and gender {}".format(
            self.name, self.email, self.gender)

    def __repr__(self):
        return self.name


def validate_email(email):

    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False


marto = Panda("Marto", "marto@pandaemail.com", "male")
pesho = Panda("Marto", "marto@pandaemail.com", "male")
