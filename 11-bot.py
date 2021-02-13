import telebot

bot = telebot.TeleBot("1613959664:AAFq5g_4mPqwg0xwHIh8BrLZDu-XXr42aJU",parse_mode=None)

@bot.message_handler(content_types=["text"])
def reply(message):
    text = message.text
    if text == "Кандай":
        text ="Ашыр Чанач"
    if text == "Салам":
        text = "Ашыр Чанач"
    if text == "Привет":
        text = "Бакыт Чанач"
    if text == "Hi":
        text = "Ашыр Чанач"
    bot.send_message(message.chat.id,text)

bot.polling()