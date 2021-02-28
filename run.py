import bot.settings
import requests
import bot.questions
from bot.questions import questions
from bot.bot_class import Bot

bot = Bot("Vasia")
bot.polling()
#bot.question()

print(bot.questions.questions["Topic"]["Topic_Name"])