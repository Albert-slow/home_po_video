import telebot
from telebot import types

my_chat_id = 409251406
bot = telebot.TeleBot(Token)  #  Создаёт объект бота

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Услуги')
    button2 = types.KeyboardButton(text='О нас')
    button3 = types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button1, button2, button3)
    bot.send_dice(message.chat.id)
    bot.send_message(message.chat.id, 'Приветствуем! Мы бухгалтерская компания! Добро пожаловать!', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Ссылка на наш сайт:', url='https://youtu.be/hp4GgkjkvyU')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Привет, нажми на кнопку и переходи на видеоролик о нас', reply_markup=keyboard)


def send_request(message):
    mes = f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку! Наши специалисты скоро с вами свяжутся.')


def send_service(message):
    bot.send_message(message.chat.id, '1 - Составить годовой отчёт')
    bot.send_message(message.chat.id, '2 - Оплатить налоги за ТОО')
    bot.send_message(message.chat.id, '3 - Рассчитать бюджет')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    elif message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Будем рады вас обслужить! Оставьте свои контактные данные.')
        bot.register_next_step_handler(message, send_request)
    elif message.text.lower() == 'услуги':
        send_service(message)


if __name__=='__main__':
    bot.infinity_polling()      # Запуск бота
