from settings import BLOCK_AFTER_N_FAILED_ATTEMPTS, BLOCK_FOR_N_MINUTES
from email_sender_controller import EmailSender


class BankController:

    def __init__(self, manager):
        self.manager = manager
        self.blocked_users = {}

    def register(self, username, password):
        if self.manager.register(username, password):
            return [True, "Registration Successfull!"]
        else:
            return [False, "Your password is not strong enough or username is already used!"]

    def login(self, username, password):
        self.update_blocked_users()
        logged_user = self.manager.login(username, password)

        if logged_user and not self.is_user_blocked(logged_user.get_username()):
            return [logged_user, "Login Successfull!"]
        else:
            # username = logged_user.get_username()
            if username in self.blocked_users.keys():
                self.blocked_users[username] += 1

                if self.blocked_users[username] >= BLOCK_AFTER_N_FAILED_ATTEMPTS:
                    self.block_user(username)
            else:
                self.blocked_users.update({username: 1})

            print (self.blocked_users)

            return [False, "Login failed!"]

    @staticmethod
    def help():
        return ["login - for logging in!", "register - for creating new account!", "reset-password - to reset your password", "exit - for closing program!"]

    @staticmethod
    def show_info(logged_user):
        result = ["You are: " + logged_user.get_username()]
        result.append("Your id is: " + str(logged_user.get_id()))
        result.append(
            "Your balance is: " + str(logged_user.get_balance()) + '$')

        return result

    def change_pass(self, new_pass, logged_user):
        pass

    def change_message(self, new_message, logged_user):
        pass

    @staticmethod
    def help_user():
        result = ["info - for showing account info"]
        result.append("changepass - for changing passowrd")
        result.append("change-message - for changing users message")
        result.append("show-message - for showing users message")
        result.append("show-email - for showing users email")
        result.append("change-email - for changing users email")

        return result

    def is_user_blocked(self, username):
        blocked_users = self.manager.get_blocked_users()
        list_blocked_users = []

        for item in blocked_users:
            list_blocked_users.append(item[0])

        return (username in list_blocked_users)

    def block_user(self, username):
        self.manager.add_blocked_user(username)
        del self.blocked_users[username]

        print ("{} is blocked! for {} minutes".format(
            username, BLOCK_FOR_N_MINUTES))

    def update_blocked_users(self):
        self.manager.update_blocked_users()

    def change_email(self, new_email, logged_user):
        self.manager.change_email(new_email, logged_user)

    def show_email(self, logged_user):
        return self.manager.get_email(logged_user.get_username())

    def validate_email(self, username, email):
        return email == self.manager.get_email(username)

    def reset_password(self, username, new_pass):
        self.manager.reset_password(username, new_pass)
        return "Successfully reset password!"

    def send_email(self, username, user_email):
        hashed_password = self.manager.get_hashed_password(username)
        EmailSender.send_email(user_email, hashed_password)

    def check_user_response(self, username, user_response):
        return user_response == self.manager.get_hashed_password(username)
