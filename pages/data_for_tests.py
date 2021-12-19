import random


class User:
    def __init__(self, username="", usermail="", userpassword=""):
        self.user_name = username
        self.user_mail = usermail
        self.user_password = userpassword

    def random_num(self):
        return str(random.choice(range(111111, 999999)))

    def fill_user_data(self):
        self.user_name = f"User{self.random_num()}"
        self.user_mail = f"BOX{self.random_num()}@testmail.com"
        self.user_password = f"MYTESTPASS{self.random_num()}"
