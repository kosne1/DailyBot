from telebot.types import Message

from app import bot


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(text='Привет! Это бот для ежедневного трека твоих задач.',
                     chat_id=message.chat.id)
