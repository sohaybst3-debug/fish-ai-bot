import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("OPENROUTER_API_KEY")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "تو دستیار هوشمند پرورش ماهی و شیلات هستی."},
                {"role": "user", "content": user_text}
            ],
        },
    )

    reply = response.json()["choices"][0]["message"]["content"]

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(8727504253:AAHPsBlN743fjGAnB6qdRdr5KPBPX_hZSzc).build()
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()
