"""Module doc string"""

import os

import openai
import streamlit as st
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def discord_hook(message):
    """_summary_"""
    if os.environ.get("ENV", "NOT_LOCAL") != "LOCAL":
        url = os.environ.get("DISCORD_HOOK", "NO_HOOK")
        if url != "NO_HOOK":
            webhook = DiscordWebhook(
                url=url, username="simple-chat-bot", content=message
            )
            webhook.execute()


discord_hook("Simple chat bot initiated")


def return_true():
    """_summary_"""
    return True


def reset_history():
    """_summary_"""
    st.session_state.openai_api_key = st.session_state.api_key
    st.session_state.messages = []


def start_app():
    """_summary_"""
    st.session_state.start_app = True
    st.session_state.openai_api_key = st.session_state.api_key


def check_openai_api_key():
    """_summary_"""
    try:
        client = OpenAI(api_key=st.session_state.openai_api_key)
        try:
            client.models.list()
        except openai.AuthenticationError as error:
            with st.chat_message("assistant"):
                st.error(str(error))
            return False
        return True
    except Exception as error:
        with st.chat_message("assistant"):
            st.error(str(error))
        return False


def main():
    """_summary_"""
    st.set_page_config(
        page_title="simple-chat-bot",
        page_icon="👾",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.title("👾👾 Simple Chat Bot 👾👾")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "openai_api_key" not in st.session_state:
        st.session_state["openai_api_key"] = None

    if "openai_maxtokens" not in st.session_state:
        st.session_state["openai_maxtokens"] = 50

    if "start_app" not in st.session_state:
        st.session_state["start_app"] = False

    if st.session_state.start_app:
        print(st.session_state.openai_api_key)
        if (
            st.session_state.openai_api_key is not None
            and st.session_state.openai_api_key != ""
        ):
            if check_openai_api_key():
                client = OpenAI(api_key=st.session_state.openai_api_key)

                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                if prompt := st.chat_input("Type your Query"):
                    with st.chat_message("user"):
                        st.markdown(prompt)
                    st.session_state.messages.append(
                        {"role": "user", "content": prompt}
                    )

                    with st.chat_message("assistant"):
                        stream = client.chat.completions.create(
                            model=st.session_state["openai_model"],
                            messages=[
                                {"role": m["role"], "content": m["content"]}
                                for m in st.session_state.messages
                            ],
                            max_tokens=st.session_state["openai_maxtokens"],
                            stream=True,
                        )
                        response = st.write_stream(stream)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
            else:
                reset_history()
        else:
            with st.chat_message("assistant"):
                st.markdown("**'OpenAI API key'** is missing.")

    with st.sidebar:
        st.text_input(
            label="OpenAI API key",
            value="",
            help="This will not be saved or stored.",
            type="password",
            key="api_key",
        )

        st.selectbox(
            "Select the GPT model", ("gpt-3.5-turbo", "gpt-4-turbo"), key="openai_model"
        )
        st.slider(
            "Max Tokens", min_value=20, max_value=80, step=10, key="openai_maxtokens"
        )
        st.button("Start Chat", on_click=start_app, use_container_width=True)
        st.button("Reset History", on_click=reset_history, use_container_width=True)


if __name__ == "__main__":
    main()
