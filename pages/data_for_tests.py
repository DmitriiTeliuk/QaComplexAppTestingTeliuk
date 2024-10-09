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


class Post:
    def __init__(self, title="", body=""):
        self.title = title
        self.post_body = body

    def generate_text(self, word_count):
        """Generate some string"""

        base_text = """Welcome to the weather forecast. 
        Now, let’s see what the weather is like today. 
        In the north of the country, it’s very windy and cold. 
        There is a chance of some rain too, so don’t leave home without your umbrella! 
        The temperature is around 10º centigrade. In the east it’s rainy all day today, 
        I’m afraid. There may be a thunderstorm in the afternoon. 
        The temperature is a bit higher, at around 13º.
        In the west and middle of the country, the weather is dry but cloudy. 
        So no rain for you, but it is quite windy and the temperature is just 10º. 
        The south of the country has the best weather today. 
        It’s cloudy most of the time but sunny this afternoon."""
        text_lst = base_text.replace("\n", " ").split(" ")
        generate_text_lst = []
        for _ in range(word_count):
            generate_text_lst.append(random.choice(text_lst))
        new_generate_text_lst = []
        # Delete all '' in the list
        for elem in generate_text_lst:
            if elem != '':
                new_generate_text_lst.append(elem)
        # make final sentence
        final_generated_text = " ".join(new_generate_text_lst)
        return final_generated_text

    def fill_post_data(self):
        self.title = self.generate_text(10)
        self.post_body = self.generate_text(20)
