import time, datetime
import telepot
import pyowm
import requests
from telepot.loop import MessageLoop
from geopy.geocoders import Nominatim
from newsapi import NewsApiClient
import sys
import re
from time import sleep
from twx.botapi import TelegramBot, ReplyKeyboardMarkup 
import traceback
from pyowm import OWM 

apiKey = '895dd3e71642adda4c6a2a1c9ad09b54'
owm = pyowm.OWM(apiKey)
newsapi = NewsApiClient(api_key='b0ac87d0931e4cdda08c441d97d9daf8')
now = datetime.datetime.now()
TOKEN = '862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ'
OWMKEY = '895dd3e71642adda4c6a2a1c9ad09b54'
bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')

def process_message(msg):
    keyboard = [['Get Weather']] 
    reply_markup = ReplyKeyboardMarkup.create(keyboard) 
    

    chat_id = msg['chat']['id'] 
    message = msg['text']
#    <command> <argument> 
#   weather accra,ghana    
    if re.match(r'hi|hello', message.lower()):
        bot.sendMessage (chat_id, 'Hi! Am Sunny , how may i help you ?')
    elif re.match(r'time', message.lower()):
        print(message)
        bot.sendMessage (chat_id, str(now.hour)+str(":")+str(now.minute))    
    elif re.match(r'weather', message.lower()):
        words = message.lower().split()
        location = words[1] +", "+ words[2]

        print(chat_id)
        print(message)
        owm = OWM(OWMKEY) 
        obs = owm.weather_at_place(location)  
        w = obs.get_weather() 
        l = obs.get_location()  
        status = str(w.get_detailed_status()) 
        placename = str(l.get_name()) 
        wtime = str(w.get_reference_time(timeformat='iso')) 
        temperature = str(w.get_temperature('celsius').get('temp'))
        
        bot.sendMessage(chat_id, 'Weather Status: ' +status +' At '+placename+' ' +wtime+' Temperature: '+ temperature+ 'C') 
    else: 
        return bot.sendMessage(chat_id, 'please select an option')
bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (bot.getMe())

MessageLoop(bot, process_message).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)