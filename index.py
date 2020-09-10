import telebot

bot = telebot.TeleBot('token :)')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi there')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'платину надо завалить камнем':
        bot.send_message(message.chat.id, 'Камень я не дам')
    else:
        bot.send_message(message.chat.id, 'say so')


bot.polling()
