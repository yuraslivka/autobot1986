import requests
import telebot
import os
import datetime
import time, random
import mail
from bs4 import BeautifulSoup
from auth_data import token



def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Ford Focus RS")




                  
        
        

    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)
