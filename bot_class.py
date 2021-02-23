import bot_token
import requests

class Bot():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

    def get_updates(self):
        response = requests.get(f"{bot_token.root_url}getUpdates")
        status = response.status_code
        if status in (200, 201, 202):
            updates = response.json()
            return updates
        else:
            raise Exception(f"request failed with status {status}")

    def last_text(self):
        response = requests.get(f"{bot_token.root_url}getUpdates")
        status = response.status_code
        if status in (200, 201, 202):
            updates = response.json()
        text = updates['result'][-1]['message']['text']
        return text

    def send_message(self, text):
        bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
            data={'chat_id': '450140685', 'text': text})



bot = Bot("Vasia")
bot.say_hello()
bot.send_message(text)
print (bot.get_updates())
print (bot.last_text())




