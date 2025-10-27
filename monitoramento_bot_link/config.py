import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
URL_MONITOR = os.getenv('URL_MONITOR', 'https://www.google.com')
PROVEDOR = os.getenv('PROVEDOR', 'claro')
REGIAO = os.getenv('REGIAO', 'sorocaba')
INTERVALO = int(os.getenv('INTERVALO', '60'))
