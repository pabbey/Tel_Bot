import time, datetime
import telepot
import pyowm
import requests
from telepot.loop import MessageLoop
from geopy.geocoders import Nominatim
from newsapi import NewsApiClient
import sys
from time import sleep
from twx.botapi import TelegramBot, ReplyKeyboardMarkup #Telegram BotAPI
import traceback
from pyowm import OWM #Weather API

apiKey = '895dd3e71642adda4c6a2a1c9ad09b54'
owm = pyowm.OWM(apiKey)
newsapi = NewsApiClient(api_key='b0ac87d0931e4cdda08c441d97d9daf8')
now = datetime.datetime.now()
TOKEN = '862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ'
OWMKEY = '895dd3e71642adda4c6a2a1c9ad09b54'


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #geolocator = Nominatim(user_agent="tel_bot")
    #location = geolocator.geocode(command)
    telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
    top_headlines = newsapi.get_top_headlines(q='sports',sources='bbc-news,',language='en')
    
    

    print ('Received: %s' % command)
    greet=("hi", "hello")

    if command.lower() in greet: #and command.lower()== 'hi'or "hellow":
        telegram_bot.sendMessage (chat_id, str("Hi! Am Sunny , how may i help you ?"))
    else:
        if command.lower() == 'time':
            telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
        #elif command == 'location' or 'LOCATION':
                #telegram_bot.sendMessage(chat_id, str(location.address))        
        elif command.lower() == 'news':#news
            telegram_bot.sendMessage(chat_id, top_headlines)
        elif command.lower() == 'weather':
            #keyboard = [['Get Weather']] #Setting a Button to Get the Weather 
            #reply_markup = ReplyKeyboardMarkup.create(keyboard) #And create the keyboard 
            #if msg.sender and msg.text and msg.chat:
                #if it is a text message then get it 
            #chat_id = msg.id 
            #user = msg.sender.username
            #command = msg.text 
            #return chat_id 
            #return message 
                #if message.lower() == 'get weather': #if the user is asking for the weather then we ask the location 
            telegram_bot.sendMessage(chat_id, 'please send me your location')
            a=(['a','b','c','s','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
                #else: 
                 #   bot.send_message(chat_id, 'please select an option', reply_markup=reply_markup).wait() #if not then just show the options
         
            if command.lower() == "ho":
                
                #text = command.text['message']['text']
                #chat = command.text['message']['chat']['id']
                
                #mm=request.get(command) 
                #if the message contains a location then get the weather on that latitude/longitude 
                #telegram_bot.sendMessage(command)
                #if command.lower() in a:
                #chat_id = mgs.message.chat.id 
                owm = OWM(OWMKEY) #initialize the Weather API 
                obs = owm.weather_at_place(command) #Create a weather observation 
                w = obs.get_weather() #create the object Weather as w 
                telegram_bot.sendMessage(chat_id, w )# <Weather - reference time=2013-12-18 09:20, status=Clouds> 
                l = obs.get_location() #create a location related to our already created weather object And send the parameters 
                status = str(w.get_detailed_status()) 
                placename = str(l.get_name()) 
                wtime = str(w.get_reference_time(timeformat='iso')) 
                temperature = str(w.get_temperature('celsius').get('temp'))
                telegram_bot.sendMessage(chat_id, 'Weather Status: ' +status +' At '+placename+' ' +wtime+' Temperature: '+ temperature+ 'C') #send the anwser
                telegram_bot.sendMessage(chat_id, 'please select an option', reply_markup=reply_markup).wait() #send the options
            
        

telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)
