from os import getenv
from pathlib import Path

import telebot
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()
# your telegram bot token
BOT_TOKEN = getenv('BOT_TOKEN')
# your google maps API key
GOOGLE_MAPS_API_KEY = getenv('GOOGLE_MAPS_API_KEY')
# creds for mailing
GMAIL_APP_LOGIN = getenv('GMAIL_APP_LOGIN')
GMAIL_APP_PASSWORD = getenv('GMAIL_APP_PASSWORD')
# googl translate creds (GET THE CREDS FILE AT GOOGLE DEVELOPER CONSOLE)
GOOGLE_TRANSLATE_CREDS_FILENAME = getenv('GOOGLE_TRANSLATE_CREDS_FILENAME')
BASE_DIR_PATH = Path(__file__).resolve().parent.parent
GOOGLE_TRANSLATE_CREDS_PATH = Path(GOOGLE_TRANSLATE_CREDS_FILENAME)
GOOGLE_APPLICATION_CREDENTIALS_PATH = str(BASE_DIR_PATH.joinpath(GOOGLE_TRANSLATE_CREDS_PATH))
# create TeleBot instance using your private BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)
