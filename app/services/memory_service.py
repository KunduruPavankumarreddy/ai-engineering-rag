from collections import deque

# Keep the last 6 messages (3 user + 3 assistant)
conversation_history = deque(maxlen=6)


def add_message(role, content):
    conversation_history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_conversation():

    history = ""

    for message in conversation_history:

        history += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    return history


def clear_memory():

    conversation_history.clear()
