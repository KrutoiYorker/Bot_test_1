import requests

#bot_token = "1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ" #@Vaverka_python_testing_bot

#bot api list
bot_api = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/getMe"
bot_updates = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/getUpdates"
bot_message = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage"

#get functions
bot_api_status = requests.get(bot_api, verify=False)
bot_updates_status = requests.get(bot_updates, verify=False)
bot_message_status = requests.get(bot_message, verify=False)

#create dict
bot_updates_dict = requests.get (bot_updates).json()

#printing for functions and dict cheking
print ("bot_message:", requests.get (bot_message).json())
print ("bot_updates:", requests.get (bot_updates).json())
print (bot_updates_dict)

#get last user's message
last_user_message = bot_updates_dict['result'][-1]['message']['text']
print ("last_user_message:", last_user_message)

# greeting function
if last_user_message == 'Привет!':
    res = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage",
                        data={"chat_id": "450140685", "text": "Привет, дорогая! Начнем тест?"})
    import requests
    bot_updates = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/getUpdates"
    bot_updates_dict = requests.get (bot_updates).json()
    last_user_message = bot_updates_dict['result'][-1]['message']['text']

if last_user_message == 'Да':
    res = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={"chat_id": "450140685", "text": "Поехали!"})
    bot_updates = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/getUpdates"
    bot_updates_dict = requests.get (bot_updates).json()
    last_user_message = bot_updates_dict['result'][-1]['message']['text']

#else:
#    res = requests.post("https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/sendMessage", data={"chat_id": "450140685", "text": "Я вас не понимаю."})

#check user message updates function
bot_updates = "https://api.telegram.org/bot1597469725:AAEMw3pImas85whqnMdH0RZsh24KP6K-qVQ/getUpdates"
bot_updates_status = requests.get(bot_updates, verify=False)
bot_updates_dict = requests.get (bot_updates).json()
last_user_message = bot_updates_dict['result'][-1]['message']['text']





