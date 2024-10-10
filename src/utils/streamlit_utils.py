"""Module doc string"""

import streamlit as st

from .constants import ConstantVariables
from .logs import logger
from .openai_utils import OpenAIFunctions


class StreamlitFunctions:
    """Module doc string"""

    @staticmethod
    def streamlit_page_config():
        """_summary_"""
        st.set_page_config(
            page_title="simple-chat-bot",
            page_icon="👾",
            layout="centered",
            initial_sidebar_state="auto",
        )
        st.title("👾👾 Simple Chat Bot 👾👾")

    @staticmethod
    def streamlit_side_bar():
        """_summary_"""
        with st.sidebar:
            st.selectbox(
                "Select Provider",
                ConstantVariables.provider,
                placeholder="Choose an option",
                key="provider_select",
            )
            if st.session_state.provider_select is not None:
                if st.session_state.provider_select == "OpenAI":
                    st.text_input(
                        label="OpenAI API key",
                        value=ConstantVariables.api_key,
                        help="This will not be saved or stored.",
                        type="password",
                        key="api_key",
                    )

                    st.selectbox(
                        "Select the GPT model",
                        ConstantVariables.model_list_tuple,
                        key="openai_model",
                    )

                elif st.session_state.provider_select == "lm-studio":
                    st.header("NOTE")
                    st.text(
                        "lm-studio is configured to work on `http://localhost:1234/v1`"
                    )

                st.slider(
                    "Max Tokens",
                    min_value=ConstantVariables.min_token,
                    max_value=ConstantVariables.max_tokens,
                    step=ConstantVariables.step,
                    key="openai_maxtokens",
                )

                st.button(
                    "Start Chat",
                    on_click=StreamlitFunctions.start_app,
                    use_container_width=True,
                )

                st.button(
                    "Reset History",
                    on_click=StreamlitFunctions.reset_history,
                    use_container_width=True,
                )

    @staticmethod
    def streamlit_initialize_variables():
        """_summary_"""
        logger.debug("Initializing Streamlit Variables")
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = ConstantVariables.default_model

        if "provider_select" not in st.session_state:
            st.session_state["provider_select"] = None

        if "openai_api_key" not in st.session_state:
            st.session_state["openai_api_key"] = None

        if "openai_maxtokens" not in st.session_state:
            st.session_state["openai_maxtokens"] = (
                ConstantVariables.default_token
            )

        if "start_app" not in st.session_state:
            st.session_state["start_app"] = False

        if "api_key" not in st.session_state:
            st.session_state["api_key"] = None

    @staticmethod
    def reset_history():
        """_summary_"""
        logger.debug("Resetting Chat State")
        st.session_state.openai_api_key = st.session_state.api_key
        st.session_state.messages = []

    @staticmethod
    def start_app():
        """_summary_"""
        logger.debug("Starting Application")
        st.session_state.start_app = True
        st.session_state.openai_api_key = st.session_state.api_key

    @staticmethod
    def streamlit_print_messages():
        """_summary_"""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    @staticmethod
    def streamlit_invoke_model():
        """_summary_"""
        if prompt := st.chat_input("Type your Query"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append(
                {"role": "user", "content": prompt}
            )
            response = OpenAIFunctions.invoke_model()
            logger.debug(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response[0]}
            )
