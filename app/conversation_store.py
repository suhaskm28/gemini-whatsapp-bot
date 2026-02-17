from collections import defaultdict

# stores conversation per user
conversations = defaultdict(list)

MAX_HISTORY = 6   # keep last 6 messages


def get_history(user_id: str):
    return conversations[user_id]


def add_message(user_id: str, role: str, content: str):
    conversations[user_id].append({
        "role": role,
        "content": content
    })

    # keep memory small
    conversations[user_id] = conversations[user_id][-MAX_HISTORY:]
