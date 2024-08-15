import openai
import streamlit as st
from openai import OpenAI

class OpenAIFunctions:
    
    @staticmethod
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