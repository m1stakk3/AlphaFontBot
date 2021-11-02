import telebot
from telebot import types

bot = telebot.TeleBot("2018392915:AAFdEpg4G1RXvY8q3B6rBCSaFP-oXLA258s", parse_mode=None)
users = []


# запуск бота + создание кнопок с примером текста
@bot.message_handler(commands=['start'])
def on_start(message: types.Message):
        name = message.from_user.username
        if name not in users:
            users.append(name)
            print(users)
        bot.send_message(message.chat.id, chr(129302) + ' Привет! Этот бот помогает оформить красиво твой профиль в соц. сетях.\nНа твой выбор здесь большое количество шрифтов.\n\nПользуйтесь с удовольствием ' + chr(128126))
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        font1 = chr(127284) + chr(127303) + chr(127280) + chr(127292) + chr(127295) + chr(127291) + chr(127284)
        buttons = [font1, 'Example', 'Example', 'Example']
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Выберите желаемый шрифт:", reply_markup=keyboard)

# обработчик текста
@bot.message_handler(content_types=['text'])
def changer(message: types.Message):
    text_from_user = message.text.lower()
    tlen = len(text_from_user)
    text_donefor_user = ''
    for i in range(tlen):
        if ord(text_from_user[i]) in range(65, 123):
            if text_from_user[i] == ' ':
                text_donefor_user += ' '
            else:
                text_donefor_user += chr(127306 - (123 - ord(text_from_user[i])))
        else:
            pass
    bot.send_message(message.chat.id, text_donefor_user)



bot.infinity_polling()
#spgspb[kbm[kmbtkrmg
