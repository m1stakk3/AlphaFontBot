import telebot
from telebot import types

bot = telebot.TeleBot("2018392915:AAFdEpg4G1RXvY8q3B6rBCSaFP-oXLA258s", parse_mode=None)
users = []
buts = [False, False, False, False]

# имена кнопок
font1 = chr(127284) + chr(127303) + chr(127280) + chr(127292) + chr(127295) + chr(127291) + chr(127284)
font2 = chr(120176) + chr(120221) + chr(120198) + chr(120210) + chr(120213) + chr(120209) + chr(120202)

# запуск бота + создание кнопок с примером текста
@bot.message_handler(commands=['start'])
def on_start(message: types.Message):
        name = message.from_user.username
        if name not in users:
            users.append(name)
            print(users)
        bot.send_message(message.chat.id, chr(129302) + ' Привет! Этот бот помогает оформить красиво твой профиль в соц. сетях.\nНа твой выбор здесь большое количество шрифтов.\n\nПользуйтесь с удовольствием ' + chr(128126))
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        buttons = [font1, font2, 'Example', 'Example']
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Выберите желаемый шрифт:", reply_markup=keyboard)

def button_listener(s):
    if s == font1:
        buts[0] = True
        return True
    if s == font2:
        buts[1] = True
        return True
    return False

# обработчик текста
@bot.message_handler(content_types=['text'])
def changer(message: types.Message):
    if button_listener(message.text):
        return
    if buts[0]:
        text_for_user = ''
        got_text = message.text.lower()
        for i in range(len(got_text)):
            if ord(got_text[i]) in range(0, 123):
                if got_text[i] == ' ':
                    text_for_user += ' '
                if got_text[i].islower() == True:
                    text_for_user += chr(127306 - (123 - ord(got_text[i])))
                else:
                    pass
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
        buts[0] = False
    if buts[1]:
        text_for_user = ''
        got_text = message.text
        for i in range(len(got_text)):
            if ord(got_text[i]) in range(0, 123):
                if got_text[i] == chr(32):
                    text_for_user += chr(32)
                if got_text[i].islower() == True:
                    text_for_user += chr(120224 - (123 - ord(got_text[i])))
                if got_text[i].isupper() == True:
                    text_for_user += chr(120197 - (90 - ord(got_text[i])))
                else:
                    pass
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
        buts[1] = False

bot.infinity_polling()