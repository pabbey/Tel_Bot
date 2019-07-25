import time, datetime
import telepot
import pyowm
from telepot.loop import MessageLoop
from geopy.geocoders import Nominatim
from newsapi import NewsApiClient

apiKey = '895dd3e71642adda4c6a2a1c9ad09b54'
owm = pyowm.OWM(apiKey)
newsapi = NewsApiClient(api_key='b0ac87d0931e4cdda08c441d97d9daf8')
now = datetime.datetime.now()

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
        telegram_bot.sendAudio(chat_id, w.get_humidity(),(w.get_wind()),(w.get_temperature(unit='celsius')),(w.get_sunrise_time()))

telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)