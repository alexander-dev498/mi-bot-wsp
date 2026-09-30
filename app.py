from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "alex123"
WHATSAPP_TOKEN = "Aca_va_tu_token_de_Meta"
PHONE_NUMBER_ID = "Aca_va_tu_phone_id"

@app.route("/whatsapp", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Error", 403

@app.route("/whatsapp", methods=["POST"])
def webhook():
    data = request.json
    try:
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]
        from_num = msg['from']
        text = msg['text']['body']

        # Aca va la respuesta de tu bot
        respuesta = f"Hola, recibi: {text}"

        url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
        headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
        payload = {
            "messaging_product": "whatsapp",
            "to": from_num,
            "text": {"body": respuesta}
        }
        requests.post(url, json=payload, headers=headers)
    except:
        pass
    return "ok", 200

if __name__ == "__main__":
    app.run()
