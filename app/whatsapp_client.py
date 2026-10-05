# Sends text and interactive button messages via the WhatsApp Graph API
import httpx
from app.config import ACCESS_TOKEN, PHONE_NUMBER_ID, GRAPH_API_VERSION

BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{PHONE_NUMBER_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


def send_text_message(to, text):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text},
    }
    httpx.post(BASE_URL, headers=HEADERS, json=payload)


def send_button_message(to, body_text, buttons):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": body_text},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": b["id"], "title": b["title"]}}
                    for b in buttons
                ]
            },
        },
    }
    httpx.post(BASE_URL, headers=HEADERS, json=payload)
