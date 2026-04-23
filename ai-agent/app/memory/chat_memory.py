# Purpose: Store conversation history per user

from collections import defaultdict

chat_store = defaultdict(list)

def add_message(user_id: str, message: str):
    chat_store[user_id].append(message)

def get_history(user_id: str):
    return chat_store[user_id][-5:]  # last 5 messages