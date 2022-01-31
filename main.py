import config as cfg
from datetime import date
from dateutil.relativedelta import relativedelta, SU
import telebot
import json

bot = telebot.TeleBot(cfg.token)
list_obj = []

def get_last_sunday():
    today = date.today()
    last_monday = today+relativedelta(weekday=SU(-1))
    return last_monday.strftime("%d.%m.%Y")

@bot.message_handler(content_types=["text"])
def main(message):
    with open('msg.txt','r') as input_f:
        list_obj = json.load(input_f)
    list_obj.append({
        'message_text': message.text
    })
    with open('msg.txt','w') as out_f:
        json.dump(list_obj, out_f)
    
    user = list_obj[-2]["message_text"]
    msg = "\n"+str(list_obj[-1]["message_text"])+"\n\n\nПользователь: "+user+"\nКурьер ... от "+get_last_sunday()

    bot.send_message(message.chat.id, msg)

if __name__ == '__main__':
    bot.infinity_polling() 