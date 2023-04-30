import telebot
from variables import *


class Bot(telebot.TeleBot):
    obj = None
    created = False

    def __init__(self, token_file_name):
        with open(token_file_name, 'r') as file:
            token = file.read()
        super().__init__(token)
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.created:
            cls.obj = super().__new__(cls)
            cls.created = True
        return cls.obj


if __name__ == "__main__":
    bot1 = Bot(TOKEN_FILE_NAME)
    bot2 = Bot(TOKEN_FILE_NAME)
    print(bot1 is bot2)

