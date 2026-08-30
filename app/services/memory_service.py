import streamlit as st


def _get_history():

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    return st.session_state.conversation_history


def add_message(role, content):

    history = _get_history()

    history.append({
        "role": role,
        "content": content
    })

    # Keep last 6 messages
    if len(history) > 6:
        history.pop(0)


def get_conversation():

    history = _get_history()

    return "\n".join(
        f"{message['role'].capitalize()}: {message['content']}"
        for message in history
    )


def clear_memory():

    st.session_state.conversation_history = []