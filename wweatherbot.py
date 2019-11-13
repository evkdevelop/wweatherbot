from colorama import init
from colorama import Fore, Back, Style
import pyowm
import telebot
import time

owm = pyowm.OWM('KEY', language = "ru")
bot = telebot.TeleBot("KEY_BOT", threaded=False)
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, "Напиши мне название Города и я скажу какая там сейчас погода")
@bot.message_handler(content_types=['text'])

def send_text(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = round( w.get_temperature('celsius')["temp"] )
        answer = "В городе " + message.text + " " + w.get_detailed_status()+".\n"
        answer += "Температура воздуха сейчас " + str(temp) + " градус(а/ов). \n\n"
        if temp<0:
            answer += "Очень холодно, а что делать? - Надевать шерстяные трусы с начесом и бегать!"
        elif temp<10:
            answer += "Холодно, а что делать? - Надевать шерстяные трусы и бегать!"
        elif temp<20:
            answer += "Тепло, а что делать? - Надевать трусы и бегать!"
        else:
            answer += "Жара, а что делать? - Снимать трусы и бегать!"


        print(Fore.GREEN, "\n\nBOT ANSWER : ", Fore.WHITE, answer + "\n\n")
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        print(Fore.RED, "ERROR : ", Fore.WHITE, str(e) + "\n\n")
        bot.send_message(message.chat.id, "Извини друг, такого города я не знаю :(")

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(Fore.RED, "ERROR : ", Fore.WHITE, str(e) + "\n\n")
        time.sleep(15)
