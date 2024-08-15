import streamlit as st


class StreamlitFunctions:
    @staticmethod
    def return_true():
        """_summary_"""
        return True

    @staticmethod
    def reset_history():
        """_summary_"""
        st.session_state.openai_api_key = st.session_state.api_key
        st.session_state.messages = []

    @staticmethod
    def start_app():
        """_summary_"""
        st.session_state.start_app = True
        st.session_state.openai_api_key = st.session_state.api_key
