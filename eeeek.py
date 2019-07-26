import time, datetime
import telepot
import pyowm
import json
import requests
from gpiozero import LED
from time import sleep
from signal import pause
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
broom =LED(18)
lroom =LED(23)
groom =LED(17)
ol = LED(27)

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
    elif message.lower() ==('on bedroom light'):
        broom.on()
        bot.sendMessage (chat_id, 'bed room light is on')
    elif message.lower() ==('off bedroom light'):
        broom.off()
        bot.sendMessage (chat_id, 'bed room light is off')
    elif message.lower() ==('on garage light'):
        groom.on()
        bot.sendMessage (chat_id, 'bed room light is on')
    elif message.lower() ==('off garage light'):
        groom.off()
        bot.sendMessage (chat_id, 'garage light is off')
    elif message.lower() ==('on living room light'):
        lroom.on()
        bot.sendMessage (chat_id, 'living room light is on')
    elif message.lower() ==('off living light'):
        lroom.off()
        bot.sendMessage (chat_id, 'living room light is off')
    elif message.lower() ==('on outside light'):
        ol.on()
        bot.sendMessage (chat_id, 'ouside light is on')
    elif message.lower() ==('off outside light'):
        ol.off()
        bot.sendMessage (chat_id, 'ol light is off')
    elif re.match(r'weather', message.lower()):
        words = message.lower().split()
        location = words[1] +", "+ words[2]

        print(chat_id)
        print(message)
        owm = OWM(OWMKEY) 
        obs = owm.weather_at_place(location)  
        w = obs.get_weather()
        hu=obs.get_humidity()
        pr=obs.get_pressure()
        l = obs.get_location()  
        status = str(w.get_detailed_status()) 
        placename = str(l.get_name()) 
        wtime = str(w.get_reference_time(timeformat='iso')) 
        temperature = str(w.get_temperature('celsius').get('temp'))
            
        bot.sendMessage(chat_id, 'Weather Status: ' +status +' At '+placename+' Date and Time for the search is: ' +wtime+'  The Temperature is: '+ temperature+ 'C' + '  The Humidity is: ' +humidity+' ' + 'The wind speed is: ' +wind+' ' + ' The Atmospheric pressure: '+pressure+' ') 
    else: 
        return bot.sendMessage(chat_id, 'Services Avialable: 1. Weather.  2.Time. 3.Home Automation'  )
bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (bot.getMe())

MessageLoop(bot, process_message).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)