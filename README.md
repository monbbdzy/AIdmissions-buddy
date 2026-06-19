# AIdmissions-buddy
AI-powered Telegram chatbot offering free, multilingual US college admissions guidance for low-income students in Central Asia.
An AI-powered Telegram chatbot built to democratize access to US college admissions guidance for low-income students across Central Asia. The bot delivers free, multilingual support — covering application strategy, financial aid, and deadlines — through a conversational interface backed by structured Python decision workflows. Built as an NGO initiative after researching the systemic barriers faced by students in the region.

## 📂 Folder Structure
```text
admissions_bot/
│
├── config/
│   ├── __init__.py
│   └── settings.py          # Bot tokens, environment variables, constant texts
│
├── database/
│   ├── __init__.py
│   └── db_handler.py        # Logic to save user language, progress, or AI logs
│
├── handlers/
│   ├── __init__.py
│   ├── start.py             # Handles /start and initial language selection
│   ├── general.py           # General Information module buttons
│   ├── tests.py             # Tests module buttons (SAT, IELTS, etc.)
│   ├── essays.py            # Essays module buttons
│   ├── common_app.py        # Common App (Honors, Activities, etc.) buttons
│   ├── css_profile.py       # CSS Profile buttons
│   └── ai_advisor.py        # Fallback "Ask AI" handling logic
│
├── keyboads/
│   ├── __init__.py
│   ├── inline.py            # Inline keyboards (attached to messages)
│   └── reply.py             # Reply keyboards (bottom of the screen)
│
├── assets/
│   ├── files/               # PDF guides, templates, worksheets to send to users
│   └── videos/              # Video links or small video clips
│
├── .env                     # Secret credentials (BOT_TOKEN, OPENAI_API_KEY)
├── requirements.txt         # List of python libraries needed
└── main.py                  # The main entry point that starts the bot

Because the bot acts like a tree structure (nested menus), the best tool to manage this in python-telegram-bot is the ConversationHandler or a state-based layout utilizing explicit callback_data.
