def extract_message(data: dict):
    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        if "messages" not in value:
            return None, None

        msg = value["messages"][0]
        sender = msg["from"]
        text = msg["text"]["body"]

        return sender, text

    except Exception as e:
        print("Parsing error:", e)
        return None, None
