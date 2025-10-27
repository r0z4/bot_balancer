import requests
from config import PROVEDOR, REGIAO, CHAT_ID, BOT_TOKEN
from telegram import Bot

def consulta_downdetector(provedor=PROVEDOR, regiao=REGIAO):
    try:
        url = f"https://downdetector.com.br/status/{provedor}/"
        r = requests.get(url)
        if r.status_code == 200:
            if regiao.lower() in r.text.lower():
                return True, f"🔴 Incidente encontrado para '{regiao}' ({provedor})"
        return False, "🟢 Nenhum incidente regional detectado."
    except Exception:
        return False, "❌ Erro ao consultar o Downdetector."

def enviar_mensagem(msg):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=msg)
