import os
from dotenv import *
from telebot import *

# Load environment variables
load_dotenv()

# Load bot token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_B")
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Bot commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm a bot!")

# Bot polling
bot.polling(
    print("Bot is running...")
)