from flask import Flask, request
import google.generativeai as genai
import os
app = Flask(__name__)
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    from twilio.twiml.messaging_response import MessagingResponse
    incoming_msg = request.values.get('Body', '')
    try:
        response = model.generate_content(f"Responde corto en español paraguayo: {incoming_msg}")
        answer = response.text[:1500]
    except Exception as e:
        answer = "Error con la API KEY, revisala en Render"
    twiml = MessagingResponse()
    twiml.message(answer)
    return str(twiml)
