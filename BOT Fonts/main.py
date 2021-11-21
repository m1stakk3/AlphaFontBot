import telebot
from telebot import types

bot = telebot.TeleBot("2018392915:AAFdEpg4G1RXvY8q3B6rBCSaFP-oXLA258s", parse_mode=None)
users = []
buttons = ['𝕰𝖝𝖆𝖒𝖕𝖑𝖊', '𝔈𝔵𝔞𝔪𝔭𝔩𝔢', '𝓔𝔁𝓪𝓶𝓹𝓵𝓮', 'ℰ𝓍𝒶𝓂𝓅𝓁𝑒', '𝐄𝐱𝐚𝐦𝐩𝐥𝐞']


eng_old_b = {'A': '𝕬', 'B': '𝕭', 'C': '𝕮', 'D': '𝕯', 'E': '𝕰', 'F': '𝕱', 'G': '𝕲', 'H': '𝕳', 'I': '𝕴',
             'J': '𝕵', 'K': '𝕶', 'L': '𝕷', 'M': '𝕸', 'N': '𝕹', 'O': '𝕺', 'P': '𝕻', 'Q': '𝕼', 'R': '𝕽',
             'S': '𝕾', 'T': '𝕾', 'U': '𝖀', 'V': '𝖁', 'W': '𝖂', 'X': '𝖃', 'Y': '𝖄', 'Z': '𝖅',
             'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊', 'f': '𝖋', 'g': '𝖌', 'h': '𝖍', 'i': '𝖎',
             'j': '𝖏', 'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓', 'o': '𝖔', 'p': '𝖕', 'q': '𝖖', 'r': '𝖗',
             's': '𝖘', 't': '𝖙', 'u': '𝖚', 'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟', ' ': ' '}

eng_old_n = {'A': '𝔄', 'B': '𝔅', 'C': '𝕮', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉', 'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ',
             'J': '𝔍', 'K': '𝔎', 'L': '𝔏', 'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ',
             'S': '𝔖', 'T': '𝔗', 'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛', 'Y': '𝔜', 'Z': 'ℨ',
             'a': '𝔞', 'b': '𝔟', 'c': '𝔠', 'd': '𝔡', 'e': '𝔢', 'f': '𝔣', 'g': '𝔤', 'h': '𝔥', 'i': '𝔦',
             'j': '𝔧', 'k': '𝔨', 'l': '𝔩', 'm': '𝔪', 'n': '𝔫', 'o': '𝔬', 'p': '𝔭', 'q': '𝔮', 'r': '𝔯',
             's': '𝔰', 't': '𝔱', 'u': '𝔲', 'v': '𝔳', 'w': '𝔴', 'x': '𝔵', 'y': '𝔶', 'z': '𝔷', ' ': ' '}

eng_hand_b = {'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘',
              'J': '𝓙', 'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡',
              'S': '𝓢', 'T': '𝓣', 'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧', 'Y': '𝓨', 'Z': '𝓩',
              'a': '𝓪', 'b': '𝓫', 'c': '𝓬', 'd': '𝓭', 'e': '𝓮', 'f': '𝓯', 'g': '𝓰', 'h': '𝓱', 'i': '𝓲',
              'j': '𝓳', 'k': '𝓴', 'l': '𝓵', 'm': '𝓶', 'n': '𝓷', 'o': '𝓸', 'p': '𝓹', 'q': '𝓺', 'r': '𝓻',
              's': '𝓼', 't': '𝓽', 'u': '𝓾', 'v': '𝓿', 'w': '𝔀', 'x': '𝔁', 'y': '𝔂', 'z': '𝔃', ' ': ' '}

eng_hand_n = {'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ', 'G': '𝒢', 'H': 'ℋ', 'I': 'ℐ',
              'J': '𝒥', 'K': '𝒦', 'L': 'ℒ', 'M': 'ℳ', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ',
              'S': '𝒮', 'T': '𝒯', 'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵',
              'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': '𝑒', 'f': '𝒻', 'g': '𝑔', 'h': '𝒽', 'i': '𝒾',
              'j': '𝒿', 'k': '𝓀', 'l': '𝓁', 'm': '𝓂', 'n': '𝓃', 'o': '𝑜', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇',
              's': '𝓈', 't': '𝓉', 'u': '𝓊', 'v': '𝓋', 'w': '𝓌', 'x': '𝓍', 'y': '𝓎', 'z': '𝓏', ' ': ' '}

eng_stan_b = {'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈',
              'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑',
              'S': '𝐒', 'T': '𝐓', 'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
              'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢',
              'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫',
              's': '𝐬', 't': '𝐭', 'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳', ' ': ' '}


# запуск бота + создание кнопок с примером текста
@bot.message_handler(commands=['start'])
def on_start(message: types.Message):
    if message.text == '/start':
        name = message.from_user.username
        if name not in users:
            users.append(name)
            print(users)
        bot.send_message(message.chat.id, chr(129302) + ' Привет! Этот бот помогает оформить красиво ' +
                                                        'твой профиль в соц. сетях.' +
                                                        '\nНа твой выбор здесь большое количество шрифтов.\n\n' +
                                                        'Пользуйтесь с удовольствием ' + chr(128126))
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "Выберите желаемый шрифт:", reply_markup=keyboard)


# читаем введенную кнопку и открываем пул под работу с ней
@bot.message_handler(func=lambda message: message.text in buttons)
def button_checker(message: types.Message):
    global active_button
    active_button = ''
    back_board = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    back_board.add('Назад')
    for i in range(len(buttons)):
        if message.text == buttons[i]:
            active_button = buttons[i]
            bot.send_message(message.chat.id, "Введите текст на английском:", reply_markup=back_board)
            break
    return active_button


# работаем с текстом
@bot.message_handler(content_types=['text'])
def check(message: types.Message):
    user_msg = message.text
    text_for_user = ''
    if message.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Выберите желаемый шрифт:", reply_markup=keyboard)
    if active_button == buttons[0]:
        for z in range(len(user_msg)):
            if user_msg[z].isalpha() or user_msg[z].isspace():
                text_for_user += eng_old_b[user_msg[z]]
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
    if active_button == buttons[1]:
        for z in range(len(user_msg)):
            if user_msg[z].isalpha() or user_msg[z].isspace():
                text_for_user += eng_old_n[user_msg[z]]
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
    if active_button == buttons[2]:
        for z in range(len(user_msg)):
            if user_msg[z].isalpha() or user_msg[z].isspace():
                text_for_user += eng_hand_b[user_msg[z]]
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
    if active_button == buttons[3]:
        for z in range(len(user_msg)):
            if user_msg[z].isalpha() or user_msg[z].isspace():
                text_for_user += eng_hand_n[user_msg[z]]
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)
    if active_button == buttons[4]:
        for z in range(len(user_msg)):
            if user_msg[z].isalpha() or user_msg[z].isspace():
                text_for_user += eng_stan_b[user_msg[z]]
            else:
                pass
        bot.send_message(message.chat.id, text_for_user)


bot.infinity_polling()
