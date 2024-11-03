#from bot.bot import Bot
#from bot.handler import MessageHandler
#from token import TOKEN
#from config import tokenbot

#TELEGRAM_TOKEN = os.getenv('token')
print("fff")

#print(tokenbot+"11")
#bot = Bot(token=tokenbot)

#def message_cb(bot, event):
#    bot.send_text(chat_id=event.from_chat, text=event.text)

#bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
#bot.start_polling()
#bot.idle()


import psycopg2
conn = psycopg2.connect(dbname='monbd', user='botpg', password='=QCciL5Z1g42ppU4M', host='46.8.71.147')
cursor = conn.cursor()


cursor.execute('SELECT * FROM themes')
records = cursor.fetchall()

print(records)




cursor.close()
conn.close()