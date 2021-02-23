import bot_token
import requests
import bot_class

from bot_class import bot
from bot_class import text
if bot.last_text() == "Привет":
    print ("Победа!")
    send_message("Это Победа!")


