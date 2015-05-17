import getpass
from sql_manager import BankDatabaseManager


# Bank Command Interface
class BankCI:

    WELCOME_MESSAGE = """Welcome to our bank service. You are not logged in.
    Please register or login"""

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        print (BankCI.WELCOME_MESSAGE)

        command = input("$$$> ")

        while command != "exit":

            if command == "register":
                self.register()

            elif command == "login":
                self.login()

            elif command == "help":
                self.help()

            elif command == "reset-password":
                self.reset_password()

            else:
                print ("Not a valid command!")

            command = input("$$$> ")

    def logged_menu(self, logged_user):
        print ("Welcome, You're logged in as: " + logged_user.get_username())

        command = input("Logged>> ")

        while command != "exit":

            if command == "info":
                self.show_info(logged_user)

            elif command == "changepass":
                self.change_pass(logged_user)

            elif command == "change-message":
                self.change_messagel(logged_user)

            elif command == "show-message":
                print(logged_user.get_message())

            elif command == "change-email":
                self.change_email(logged_user)

            elif command == "show-email":
                self.show_email(logged_user)

            elif command == "help":
                self.help_user()

            else:
                print ("Not a valid command!")

            command = input("Logged>> ")

    def register(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        reg_status = self.controller.register(username, password)

        while not reg_status[0]:
            print (reg_status[1])
            username = input("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password: ")
            reg_status = self.controller.register(username, password)

        print (reg_status[1])

    def login(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        login_status = self.controller.login(username, password)

        if login_status[0]:
            self.logged_menu(login_status[0])
        else:
            print (login_status[1])

    def help(self):
        for line in self.controller.help():
            print (line)

    def show_info(self, logged_user):
        for line in self.controller.show_info(logged_user):
            print (line)

    def change_pass(self, logged_user):
        pass

    def change_message(self, logged_user):
        pass

    def change_email(self, logged_user):
        new_email = input("Enter new email: ")
        self.controller.change_email(new_email, logged_user)

        print("Email changed!")

    def show_email(self, logged_user):
        pass

    def help_user(self):
        for line in self.controller.help_user():
            print (line)

    def reset_password(self):
        username = input('Your username> ')
        user_email = input('Your email> ')
        is_email_valid = self.controller.validate_email(username, user_email)

        if is_email_valid:
            self.controller.send_email(username, user_email)
            response = input('Enter code from email> ')
            is_response_valid = self.controller.check_user_response(
                username, response)

            if is_response_valid:
                new_password = getpass.getpass(
                    prompt="Enter your new password: ")

                while BankDatabaseManager.validate_password(username, new_password) is False:
                    new_password = getpass.getpass(
                        prompt="Enter your new password: ")

                print (self.controller.reset_password(username, new_password))
            else:
                print ("Wrong code!")
        else:
            print ("Invalid email!")