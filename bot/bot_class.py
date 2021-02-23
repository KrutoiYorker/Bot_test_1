from . import settings
import requests

class Bot():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

    def get_updates(self):
        response = requests.get(f"{settings.root_url}getUpdates")
        status = response.status_code
        if status in (200, 201, 202):
            updates = response.json()
            return updates
        else:
            raise Exception(f"request failed with status {status}")

    def last_text(self):
        response = requests.get(f"{settings.root_url}getUpdates")
        status = response.status_code
        if status in (200, 201, 202):
            updates = response.json()
        text = updates['result'][-1]['message']['text']
        return text

    def send_message(self, text):
        bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
            data={'chat_id': '450140685', 'text': text})

    def polling(self):
        last_message_id = 0
        while True:
            response = requests.get(f"{settings.root_url}getUpdates")
            status = response.status_code
            if status in (200, 201, 202):
                updates = response.json()
            dynamic_last_message_id = updates['result'][-1]['message']['message_id']
            if dynamic_last_message_id > last_message_id:
                self.send_message("Hello!")
                last_message_id = dynamic_last_message_id






