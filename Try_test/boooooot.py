import time, datetime
import telepot
import pyowm
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



bot = TelegramBot(TOKEN) 
bot.update_bot_info().wait()  #wait for a message
print (bot.username) 
last_update_id = 0 

    

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    geolocator = Nominatim(user_agent="tel_bot")
    location = geolocator.geocode(command)
    telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
    top_headlines = newsapi.get_top_headlines(q='sports',sources='bbc-news,',language='en')
    observation1 = owm.weather_at_place('Ghana')
    w = observation1.get_weather()
    

    print ('Received: %s' % command)

    if command == 'hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Am Sunny , how may i help you ?"))
    elif command == 'time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    #elif command == 'location' or 'LOCATION':
            #telegram_bot.sendMessage(chat_id, str(location.address))        
    elif command == 'news':
        telegram_bot.sendDocument(chat_id, top_headlines)
    elif command == 'weather':
        
        def process_message(bot, u): #This is what we'll do when we get a message 
    #Use a custom keyboard 
            keyboard = [['Get Weather']] #Setting a Button to Get the Weather 
            reply_markup = ReplyKeyboardMarkup.create(keyboard) #And create the keyboard 
            if u.message.sender and u.message.text and u.message.chat: #if it is a text message then get it 
                chat_id = u.message.chat.id 
                user = u.message.sender.username
                message = u.message.text 
                return chat_id 
                return message 
                if message == 'Get Weather': #if the user is asking for the weather then we ask the location 
                    bot.send_message(chat_id, 'please send me your location') 
                else: 
                    bot.send_message(chat_id, 'please select an option', reply_markup=reply_markup).wait() #if not then just show the options
         
            elif u.message.location: #if the message contains a location then get the weather on that latitude/longitude 
                return u.message.location 
                chat_id = u.message.chat.id 
                owm = OWM(OWMKEY) #initialize the Weather API 
                obs = owm.weather_at_coords(u.message.location.latitude, u.message.location.longitude) #Create a weather observation 
                w = obs.get_weather() #create the object Weather as w 
                return w # <Weather - reference time=2013-12-18 09:20, status=Clouds> 
                l = obs.get_location() #create a location related to our already created weather object And send the parameters 
                status = str(w.get_detailed_status()) 
                placename = str(l.get_name()) 
                wtime = str(w.get_reference_time(timeformat='iso')) 
                temperature = str(w.get_temperature('celsius').get('temp'))
                bot.send_message(chat_id, 'Weather Status: ' +status +' At '+placename+' ' +wtime+' Temperature: '+ temperature+ 'C') #send the anwser
                bot.send_message(chat_id, 'please select an option', reply_markup=reply_markup).wait() #send the options again
            else: 
                return u.bot.send_message(chat_id, 'please select an option', reply_markup=reply_markup).wait() 
        while True: #a loop to wait for messages
            updates = bot.get_updates(offset = last_update_id).wait() #we wait for a message
            try: 
                for update in updates: #get the messages
                    if int(update.update_id) > int(last_update_id): #if it is a new message then get it
                        last_update_id = update.update_id 
                        process_message(bot, update) #send it to the function 
                        continue 
                continue 
            except Exception: 
                ex = None 
                print (traceback.format_exc() )
                continue
        return process_message(bot, update)       
    telegram_bot.sendMessage(chat_id,str(process_message(bot, update)))

telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)