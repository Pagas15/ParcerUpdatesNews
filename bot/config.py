import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')

ADMINS_ID = [int(admin.strip()) for admin in os.getenv('TELEGRAM_ADMIN_ID').split(',')]
