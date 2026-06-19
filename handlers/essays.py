# handlers/essays.py
from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import get_sub_menu, get_main_menu

async def show_essays_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text="Welcome to the **Essays Module**. Here you can find resources for Personal Statements and Supplements.",
        reply_markup=get_sub_menu("essays"),
        parse_mode="Markdown"
    )

async def handle_essays_subbuttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data # e.g., "essays_files"
    
    if data == "essays_about":
        await query.edit_message_text("This section covers brainstorming, drafting, and refining essays...", reply_markup=get_sub_menu("essays"))
    elif data == "essays_files":
        # Send a PDF guide from your assets folder
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open('assets/files/essay_guide.pdf', 'rb'))