import telebot

# Подставьте сюда токен Вашего бота
TOKEN = '7546967677:AAFIuOROtRfs9MH-WUn9Y7NJcrZGE0Iekoo'
bot = telebot.TeleBot(7546967677:AAFIuOROtRfs9MH-WUn9Y7NJcrZGE0Iekoo)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    youtube_button = telebot.types.InlineKeyboardButton(text="YouTube", web_app=telebot.types.WebAppInfo(url="https://www.youtube.com"))
    keyboard.add(youtube_button)
    bot.send_message(message.chat.id, "Нажмите кнопку для открытия YouTube:", reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling()
