# FastAPI app, webhook routes, and Lambda entry point
from fastapi import FastAPI, Request
from mangum import Mangum
from app.config import VERIFY_TOKEN
from app.responses import RESPONSES
from app.whatsapp_client import send_text_message, send_button_message

app = FastAPI()


@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return {"error": "invalid verify token"}


@app.post("/webhook")
async def handle_webhook(request: Request):
    body = await request.json()

    try:
        entry = body["entry"][0]
        change = entry["changes"][0]["value"]
        message = change["messages"][0]
        sender = message["from"]
    except (KeyError, IndexError):
        return {"status": "ignored"}

    if message["type"] == "text":
        text = message["text"]["body"].strip().lower()
        reply = RESPONSES.get(text)
        if reply:
            send_button_message(sender, reply["body"], reply["buttons"])
        else:
            send_text_message(sender, "Sorry, I didn't understand that.")

    elif message["type"] == "interactive":
        button_id = message["interactive"]["button_reply"]["id"]
        reply = RESPONSES.get(button_id)
        if reply:
            send_button_message(sender, reply["body"], reply["buttons"])

    return {"status": "ok"}


handler = Mangum(app)
