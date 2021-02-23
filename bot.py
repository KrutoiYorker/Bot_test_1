import bot_token
import requests
import bot_class



"""
def get_updates():
    response = requests.get(f"{root_url}getUpdates")
    status = response.status_code
    if status in (200, 201, 202):
        updates = response.json()
        return updates
    else:
        raise Exception(f"request failed with status {status}")

print(get_updates())
"""
"""
def last_text():
    updates = get_updates()
    text = updates['result'][-1]['message']['text']
    return text
print (last_text())

last_text = last_text()
if last_text == 'Привет':
    bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id': '450140685', 'text': 'Привет, дорогая! Начнем тест?'})




def is_bot():
	updates = get_updates()
	bot_answered = updates['result'][-1]['message']['from']['is_bot']
	if bot_answered == True:
		is_bot = True
	if bot_answered == False:
		is_bot = False
	else:
		print('Внимание ошибка в функции is_bot')
	return is_bot

last_text = last_text()
if last_text == 'Привет':


def last_phrase_check():
	is_bot = is_bot()
	while is_bot == True:
		updates = get_updates()
	else:
		last_text = last_text()
		if last_text == 'Привет':
			bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id':'450140685', 'text':'Привет, дорогая! Начнем тест?'})
		if last_text == 'Да':
			bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id': '450140685', 'text': 'Вопрос №1'})
		else:
			bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id': '450140685', 'text': 'Чё?'})
	return (bot_answer)
"""


