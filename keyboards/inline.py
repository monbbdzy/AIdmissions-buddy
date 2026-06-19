# keyboards/inline.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📖 General Info", callback_data="menu_general")],
        [InlineKeyboardButton("📝 Tests", callback_data="menu_tests")],
        [InlineKeyboardButton("✍️ Essays", callback_data="menu_essays")],
        [InlineKeyboardButton("🏫 Common App", callback_data="menu_common_app")],
        [InlineKeyboardButton("💰 CSS Profile", callback_data="menu_css")],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_sub_menu(module_name: str):
    """Generates the universal sub-buttons for each module"""
    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data=f"{module_name}_about")],
        [InlineKeyboardButton("📁 Files", callback_data=f"{module_name}_files")],
        [InlineKeyboardButton("🎥 Videos", callback_data=f"{module_name}_videos")],
        [InlineKeyboardButton("💡 Advice", callback_data=f"{module_name}_advice")],
        [InlineKeyboardButton("🤖 Ask AI", callback_data=f"{module_name}_ai")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)