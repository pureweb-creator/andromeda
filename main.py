import config as cfg
from datetime import date
from dateutil.relativedelta import relativedelta, SU
import telebot
from telebot import types
import json

bot = telebot.TeleBot(cfg.token)
filepath = "src/msg.txt"
list_obj = []

def get_last_sunday():
    today = date.today()
    last_monday = today+relativedelta(weekday=SU(-1))
    return last_monday.strftime("%d.%m.%Y")

# buttons
mm = types.ReplyKeyboardMarkup(row_width=2)
button1  = types.KeyboardButton("Алтай")
button2  = types.KeyboardButton("Пабло")
button3  = types.KeyboardButton("Пино")
button4  = types.KeyboardButton("Птица")
button5  = types.KeyboardButton("Дёс")
button6  = types.KeyboardButton("Тайлер")
button7  = types.KeyboardButton("Жаба")
button8  = types.KeyboardButton("Настя")
button9  = types.KeyboardButton("Майки")
button10 = types.KeyboardButton("Влад")
button11 = types.KeyboardButton("Литр")
button12 = types.KeyboardButton("Ювелир")
button13 = types.KeyboardButton("Док")
button13 = types.KeyboardButton("...")
mm.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13)

@bot.message_handler(content_types=["text"])
def main(message):
    with open(filepath,'r') as input_f:
        list_obj = json.load(input_f)

    del list_obj[:-12] #clear file

    list_obj.append({
        'message_text': message.text
    })
    with open(filepath,'w') as out_f:
        json.dump(list_obj, out_f)
    
    user = list_obj[-3]["message_text"]
    courier = list_obj[-1]["message_text"]
    msg = "\n"+str(list_obj[-2]["message_text"])+"\n\n\nПользователь: "+user+"\nКурьер: "+courier+" от "+get_last_sunday()

    bot.send_message(message.chat.id, msg, reply_markup=mm)

if __name__ == '__main__':
    bot.infinity_polling() 