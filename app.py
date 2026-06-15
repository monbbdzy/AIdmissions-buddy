# Admissions Bot
# There are basic commands using which you can get basic info, materials and useful links
# Additionally since the bot is AI, users can ask questions about admissions => make the bot remember the history
# Your AI admissions buddy
# Based on your knowledge the bot presents to you relatable information - noob | pro | hacker (something like this)

#Imports
import os
from huggingface_hub import InferenceClient

from typing import Final #is a hint that indicates that variable should not be reassigned
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup #Each time a user interacts with the bot, Telegram sends an Update object.
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv

load_dotenv()

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

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE): # pauses, lets other things run meanwhile
    keyboard = [
        [InlineKeyboardButton('Õzbek tili 🇺🇿', callback_data='uzbek')],
        [InlineKeyboardButton('Русский язык 🇷🇺', callback_data='russian')],
        [InlineKeyboardButton('English 🇬🇧', callback_data='english')]
        # You can add more buttons like this:
        # [InlineKeyboardButton('Another button', callback_data='option2')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Hello! I am your admissions buddy! Please choose the language you prefer:',
        reply_markup=markup
    )

# Buttons
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    language_selected = query.data
    context.user_data['language'] = language_selected  # Store it per user

    await query.edit_message_text(text=f"Language selected: {language_selected.capitalize()}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): # pauses, lets other things run meanwhile
    await update.message.reply_text('Meov! Please type something so I can respond :3')


# Responses
def handle_response(prompt:str, language_selected: str = "english") -> str: #text: str is a hint to the type of argument that needs to be put 
    # -> str: is a hint for the output (just like in C++)
    # AI model from hf
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[
            {
                "role" : "system",
                "content" : f"USA admissions buddy, language = {language_selected}"
            },
            {
                "role" : "user",
                "content" : prompt
            }
        ],
    ) 
    return completion.choices[0].message.content

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'Update({update.message.chat.id}) in {message_type}: "{text}"') #For checking everything
    language = context.user_data.get("language", "english")
    
    if message_type == 'group': #If the message is in group
        if BOT_USERNAME in text: #reply only if the username of bot is included in that message 
            new_text: str = text.replace(BOT_USERNAME, '').strip() #remove the bot username and send the reply to the handle response function
            response: str = handle_response(new_text)

        else:
            return
        
    else:
        response: str = handle_response(text, language)

    print('Bot:', response) #Print functions to check for any errors
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE): #function to determine any type of errors
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__': #Main function #it means Only run this block if this script is being executed directly, not imported as a module.
    print('Starting the bot...')
    app = Application.builder().token(TOKEN).build() #Building the app using the given token 
    #Application is a class provided by python-telegram-bot library -> THIS IS YOUR BOT ENGINE
    #Application.builder() -> creates an instance of the application class
    #.token(TOKEN) -> connects our this script to telegram using the token
    # build() -> finalizes everything and gives us the app.

    #Commands
    app.add_handler(CommandHandler('start', start_command)) #Initiating defined commands that appear when commands are typed 
    app.add_handler(CommandHandler('help', help_command)) #add_handler tells the bot what to do when messages are sent to it

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message)) #Initiating function that deals with the messages
    #filters.text only is initiated when text messages are sent not images or videos 

    #Buttons
    app.add_handler(CallbackQueryHandler(language_callback))
    
    #Error
    app.add_error_handler(error) #Function that reports the errors

    #Polls the bot 
    print('Polling...') 
    app.run_polling(poll_interval=4) #Constantly checks telegram for any new updates(messages)