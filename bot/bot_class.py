from . import settings
import requests
from . import questions

logger = setting.logging
class Bot():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

    def get_updates(self):
        try:
            response = requests.get(f"{settings.root_url}getUpdates")
            status = response.status_code
            if status in settings.ok_codes:
                updates = response.json()
                print (f"Updates was successful. Status{status}")
                logger.warning(f"Updates was successful. Status{status}")
            return updates
            else:
                logger.warning(f"Updates was not get successful. Status{status}"\n))

return result

        except Exception as e:
            raise Exception(f"Request failed as: {e}")

    def last_text(self):
        updates = self.get_updates()
        text = updates['result'][-1]['message']['text']
        return text

    def send_message(self, text):
        try:
            bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
                data={'chat_id': '450140685', 'text': text})
            if status in settings.ok_codes:
                updates = response.json()
                return updates
            else:
                result = {"ok": False, "error_message": f"Response code:{status}"}
            return result

        except Exception as e:
            raise Exception(f"Request failed as: {e}")


    def polling(self):
        last_message_id = 0
        while True:
            updates = self.get_updates()
            dynamic_last_message_id = updates['result'][-1]['message']['message_id']
            text = self.last_text()
            if dynamic_last_message_id > last_message_id:
                if text == "Привет!":
                    self.send_message("Привет! Начнем тест?")
                    last_message_id = dynamic_last_message_id
            else:
                print (f"Cant't take updates : {updates}{error_message}")


"""                 
        
    def question(self, question, possible_answers):
        question = 1 #questions['Topic']
        possible_answers = 2 #questions['Level']
           # question = questions['Qestions_info]['Question_text']
          #  possible_answers = questions['Qestions_info']['Possible_answers']                                                                                    ''
        bot_question = requests.post(
                "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
                data={'chat_id': '450140685', 'text': question})
        bot_possible_answers = requests.post(
               "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
               data={'chat_id': '450140685', 'text': possible_answers})
"""






