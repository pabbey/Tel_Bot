import time, datetime
import telepot
from telepot.loop import MessageLoop
from geopy.geocoders import Nominatim
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b0ac87d0931e4cdda08c441d97d9daf8')

now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(command)
    

    print ('Received: %s' % command)

    if command == 'hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Am Sunny , how may i help you ?"))
    elif command == 'time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == 'location':
            telegram_bot.sendMessage(chat_id, str(location.address))        
    elif command == 'news':
        telegram_bot.sendDocument(chat_id, str(top_headlines = newsapi.get_top_headlines(q='bitcoin',sources='bbc-news,',category='business',language='en')))
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))

telegram_bot = telepot.Bot('862774896:AAEA56RsA0Od0rxBA49vGr5zoASSD-NQySQ')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)