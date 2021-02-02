import requests

bot_token = "1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ"  # @Vaverka_python_testing_bot

root_url = f"https://api.telegram.org/bot{bot_token}/"


def get_updates():
    response = requests.get(f"{root_url}getUpdates")
    status = response.status_code
    if status in (200, 201, 202):
        updates = response.json()
        return updates
    else:
        raise Exception(f"request failed with status {status}")


print(get_updates())

def last_user_text():
    updates = get_updates()
    text = updates['result'][-1]['message']['text']
    return text
print (last_user_text())

def last_phrase_check():
	updates = get_updates()
	is_bot_answered = updates['result'][-1]['message']['from']['is_bot']
	if is_bot_answered == True:
		while is_bot_answered == True:
			print (get_updates().json) #будет ли работать функция без присвоения ее переменной?
	if is_bot_answered == False:
		user_answer = last_user_text()
		if user_answer == 'Привет':
			bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id':'450140685', 'text':'Привет, дорогая! Начнем тест?'})
		if user_answer == 'Да':
			bot_answer = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={'chat_id': '450140685', 'text': 'Вопрос №1'})
		else:
			raise Exception("ошибка")
	else:
		print("Непредвитденнная ошибка")
	return (bot_answer)

print(last_phrase_check().json)
