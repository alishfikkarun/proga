from flask import Flask, request
from telegram import Bot, LabeledPrice

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"
PROVIDER_TOKEN = "TELEGRAM_STARS_PROVIDER_TOKEN"  # важно!
bot = Bot(BOT_TOKEN)

@app.route("/buy-stars", methods=["POST"])
def buy_stars():
    data = request.get_json()
    stars = int(data.get("stars"))
    user_id = data.get("user_id")

    # Цена в Stars — передаётся в копейках
    prices = [LabeledPrice(label=f"{stars} звёзд", amount=stars * 100)]  # 1 star = 100 (внутренние единицы)

    bot.send_invoice(
        chat_id=user_id,
        title="Покупка звёзд",
        description=f"Вы покупаете {stars} звёзд",
        payload="stars-purchase",
        provider_token=PROVIDER_TOKEN,
        currency="USD",  # у Stars сейчас поддерживается только USD
        prices=prices,
        start_parameter="stars-purchase",
        is_flexible=False
    )

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
