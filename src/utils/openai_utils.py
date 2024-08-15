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
            except openai.AuthenticationError as error:
                with st.chat_message("assistant"):
                    st.error(str(error))
                logger.error(str(error))
                return False
            return True
        except Exception as error:
            with st.chat_message("assistant"):
                st.error(str(error))
            logger.error(str(error))
            return False
