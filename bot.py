import requests

bot_token = "1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ" #@Vaverka_python_testing_bot

root_url=f"https://api.telegram.org/bot{bot_token}/"


def get_updates():
	response=requests.get(f"{root_url}getUpdates")
	status=response.status_code
	if status in (200, 201, 202):
		updates=response.json()
		return updates
	else:
		raise Exception(f"request failed with status {status}")

print(get_updates())