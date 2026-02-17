from fastapi import Request
from app.utils import extract_message
from app.gemini_service import generate_reply
from app.whatsapp_service import send_message
from app.conversation_store import get_history, add_message


async def process_webhook(request: Request):
    data = await request.json()

    sender, message = extract_message(data)

    if not sender or not message:
        return {"status": "ignored"}

    print(f"📩 Message from {sender}: {message}")

    # save user message
    add_message(sender, "User", message)

    # build conversation context
    history = get_history(sender)
    context = "\n".join([f"{m['role']}: {m['content']}" for m in history])

    # generate reply using context
    reply = await generate_reply(context)

    print("🤖 AI Reply:", reply)

    # save assistant reply
    add_message(sender, "Assistant", reply)

    send_message(sender, reply)

    return {"status": "processed"}
