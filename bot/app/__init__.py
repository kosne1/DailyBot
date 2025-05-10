from telebot import TeleBot

from app.configs import env

bot = TeleBot(token=env.TG_BOT_API_TOKEN, parse_mode='html')
