import telebot


TOKEN = "6888803888:AAH_a7FrxsjICL1DcGX2nh_s4jUXSZaQllc"

bot = telebot.TeleBot(TOKEN)


markup_1 = telebot.types.InlineKeyboardMarkup()
conclusion = telebot.types.InlineKeyboardButton(text="Вывод", callback_data="djfkdl" , switch_inline_query='test')
add = telebot.types.InlineKeyboardButton(text='Пополнить' , callback_data="JJJJ" , switch_inline_query='test')

markup_1.add(conclusion, add)


def f():
    print("hello")

@bot.message_handler(commands=['dog'])
def send(message):
    bot.send_photo(message.chat.id , photo="https://banner2.cleanpng.com/20180422/rue/kisspng-dog-animation-cartoon-clip-art-cartoon-forest-5adc91d33b5b49.3768177615244046912431.jpg")


btn_1 = telebot.types.InlineKeyboardButton(text="github" , url="github.com")
btn_2 = telebot.types.InlineKeyboardButton(text="balance", callback_data="add")

markup = telebot.types.InlineKeyboardMarkup().add(btn_1 , btn_2)
    



@bot.message_handler(commands=['start'])
def go(message):
    bot.send_message(message.chat.id , text="Hello" , reply_markup=markup)

@bot.callback_query_handler(f())
def go(callback):
    bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.id,
        text="Data:",
        reply_markup=markup_1
    )

bot.polling()

