class BankController:

    def __init__(self, manager):
        self.manager = manager

    def register(self, username, password):
        pass

    def login(self, username, password):
        pass

    @staticmethod
    def help():
        return ["login - for logging in!", "register - for creating new account!", "exit - for closing program!"]

    @staticmethod
    def show_info(logged_user):
        result = ["You are: " + logged_user.get_username()]
        result.append("Your id is: " + str(logged_user.get_id()))
        result.append(
            "Your balance is:" + str(logged_user.get_balance()) + '$')

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

        return result
