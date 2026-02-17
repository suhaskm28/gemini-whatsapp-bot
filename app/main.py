from fastapi import FastAPI, Request
from app.webhook_handler import process_webhook
from app.config import VERIFY_TOKEN

app = FastAPI()


@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "Verification failed"}


@app.post("/webhook")
async def webhook(request: Request):
    return await process_webhook(request)
