"""Module doc string"""

import streamlit as st
from .logs import logger
from .constants import ConstantVariables


class StreamlitFunctions:
    """Module doc string"""

    @staticmethod
    def streamlit_page_config():
        st.set_page_config(
            page_title="simple-chat-bot",
            page_icon="👾",
            layout="centered",
            initial_sidebar_state="auto",
        )
        st.title("👾👾 Simple Chat Bot 👾👾")

    @staticmethod
    def streamlit_initialize_variables():
        """_summary_"""
        logger.debug("Initializing Streamlit Variables")
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = ConstantVariables.default_model

        if "openai_api_key" not in st.session_state:
            st.session_state["openai_api_key"] = None

        if "openai_maxtokens" not in st.session_state:
            st.session_state["openai_maxtokens"] = ConstantVariables.default_token

        if "start_app" not in st.session_state:
            st.session_state["start_app"] = False

    @staticmethod
    def return_true():
        """_summary_"""
        return True

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
