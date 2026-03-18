from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "pon aquí tu token de Telegram Bot"


def procesar_video(ruta_video: str):
    print(f"Procesando vídeo: {ruta_video}")
    
    # Aquí haces tus cálculos
    # Por ejemplo:
    # - leer frames con OpenCV
    # - sacar medidas
    # - analizar movimiento
    # - guardar resultados
    
    resultado = "Cálculo terminado correctamente"
    return resultado


async def recibir_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    if not video:
        await update.message.reply_text("No he recibido ningún vídeo.")
        return

    await update.message.reply_text("Vídeo recibido. Lo estoy descargando...")

    archivo = await video.get_file()
    ruta_guardado = "video_recibido.mp4"
    await archivo.download_to_drive(ruta_guardado)

    await update.message.reply_text("Vídeo descargado. Ahora lo proceso...")

    resultado = procesar_video(ruta_guardado)

    await update.message.reply_text(f"Resultado: {resultado}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.VIDEO, recibir_video))

app.run_polling()