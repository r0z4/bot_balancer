from telegram.ext import Application, CommandHandler
import threading
import time
from config import BOT_TOKEN, INTERVALO
from monitor import checar_link
from utils import consulta_downdetector, enviar_mensagem

async def status(update, context):
    if checar_link():
        await update.message.reply_text("✅ Link de internet OK no momento.")
    else:
        await update.message.reply_text("❌ Link fora! Verificando região...")
        ok, info = consulta_downdetector()
        await update.message.reply_text(info)

async def help_cmd(update, context):
    await update.message.reply_text(
        "/status - Verificar status atual\n/help - Lista de comandos"
    )

def rodar_monitoramento():
    while True:
        if not checar_link():
            enviar_mensagem("🚨 Internet OFF! Checando incidentes...")
            ok, info = consulta_downdetector()
            enviar_mensagem(info)
        time.sleep(INTERVALO)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_cmd))

    t = threading.Thread(target=rodar_monitoramento, daemon=True)
    t.start()

    app.run_polling()
