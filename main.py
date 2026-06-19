
'''
 Name         : app.py
 Author       : Nigina Rashidova
 Version      : 1
 Date Created : 2/6/2025
 Date Modified: 18/6/2026
 Description  : AIdmissions buddy telegram bot script 
'''

#Imports
import os
from huggingface_hub import InferenceClient

import logging
from typing import Final #is a hint that indicates that variable should not be reassigned
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup #Each time a user interacts with the bot, Telegram sends an Update object.
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv

load_dotenv()

#you will know when (and why) things don't work as expected:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Application - The central bot object. It handles polling, dispatching handlers, and managing context.
#CommandHandler - Handles commands like`/start`, /help, etc.
#MessageHandler - handles non command messages like text, images etc ...
#filters - A module (not a class) that defines filters like filters.TEXT, filters.COMMAND, etc.
#ContextTypes - defines types of the context for command handler
TOKEN: Final = os.getenv('TELEGRAM_API_TOKEN')
BOT_USERNAME: Final = '@Rashidovamimibot'

#AI hugging face
client = InferenceClient(
    provider="together",
    api_key= os.getenv('HF_API_KEY'),
)

# main.py
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config.settings import BOT_TOKEN
from handlers import start, essays # import your handler files

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Base commands
    app.add_handler(CommandHandler("start", start.start_command))

    # Routing the menu selections
    app.add_handler(CallbackQueryHandler(essays.show_essays_menu, pattern="^menu_essays$"))
    app.add_handler(CallbackQueryHandler(essays.handle_essays_subbuttons, pattern="^essays_"))
    
    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()