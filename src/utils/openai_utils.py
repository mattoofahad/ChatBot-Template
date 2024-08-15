"""Module doc string"""

import openai
import streamlit as st
from openai import OpenAI
from .logs import logger, log_execution_time


class OpenAIFunctions:
    """Module doc string"""

    @log_execution_time
    @staticmethod
    def check_openai_api_key():
        """_summary_"""
        logger.info("Checking OpenAI Key")
        try:
            client = OpenAI(api_key=st.session_state.openai_api_key)
            try:
                client.models.list()
                logger.error("OpenAI key Working")
                return True
            except openai.AuthenticationError as auth_error:
                with st.chat_message("assistant"):
                    st.error(str(auth_error))
                logger.error("AuthenticationError: %s", auth_error)
                return False
            except openai.OpenAIError as openai_error:
                with st.chat_message("assistant"):
                    st.error(str(openai_error))
                logger.error("OpenAIError: %s", openai_error)
                return False
        except Exception as general_error:
            with st.chat_message("assistant"):
                st.error(str(general_error))
            logger.error("Unexpected error: %s", general_error)
            return False
