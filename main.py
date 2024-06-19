import telebot
from telebot import types

#Conexión con BOT
TOKEN = '6962939147:AAHmuaMwJgEjp6IdQDkxvwGayh4EiA98EBw'
bot = telebot.TeleBot(TOKEN)


#Creación de comandos '/start' y '/help'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! Soy el 1er bot de Alvaro creado con Telebot')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Puedes interactuar conmigo usando comandos. Por ahora, solo /start y /help")

@bot.message_handler(commands=['thais'])
def send_thais(message):
    bot.reply_to(message, 'Mi novia bella')


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands = ['pizza'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    #Creación de botones
    btn_si = types.InlineKeyboardButton('Si', callback_data='pizza_si')
    btn_no = types.InlineKeyboardButton('No', callback_data='pizza_no')


    #Agrega botones al markup
    markup.add(btn_si, btn_no)

    #Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Te gusta la pizza?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'pizza_si':
        bot.answer_callback_query(call.id, '¡A mí también!')
    elif call.data == 'pizza_no':
        bot.answer_callback_query(call.id, 'Cada uno sus gustos...')


@bot.message_handler(commands = ['mj'])
def send_image(message):
    img_url = 'https://f4.bcbits.com/img/a1937475638_65'
    bot.send_photo(chat_id=message.chat.id, photo = img_url, caption='Aquí tienes tu imagen')






if __name__  == "__main__":
    bot.polling(non_stop=True)
