from flask import Flask, request, send_from_directory
from telegram import Bot, LabeledPrice
import os

app = Flask(__name__)
bot = Bot(token="7456960751:AAEIAM3QPYMkOPETG_Pnr43VZJxFxQXzfp4")

@app.route("/")
def index():
    return send_from_directory("webapp", "index.html")

@app.route("/script.js")
def js():
    return send_from_directory("webapp", "script.js")

@app.route("/buy", methods=["POST"])
def buy_stars():
    data = request.get_json()
    stars = int(data["stars"])
    user_id = int(data["user_id"])

    bot.send_invoice(
        chat_id=user_id,
        title="Покупка цифрового товара",
        description=f"{stars} звёзд",
        payload="star-purchase",
        provider_token=None,  # НЕ передаём токен
        currency="XTR",       # ВАЛЮТА ДЛЯ ЗВЁЗД
        prices=[LabeledPrice(label=f"{stars} звёзд", amount=stars * 100)],
        is_flexible=False,
        start_parameter="stars"
    )

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
