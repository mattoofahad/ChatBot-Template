"""Module doc string"""

from datetime import datetime

import streamlit as st
from .utils import (
    OpenAIFunctions,
    StreamlitFunctions,
    discord_hook,
    logger,
)

datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
discord_hook(f"Simple chat bot initiated {datetime_string}")


def main():
    """_summary_"""
    StreamlitFunctions.streamlit_page_config()
    StreamlitFunctions.streamlit_initialize_variables()
    StreamlitFunctions.streamlit_side_bar()
    if st.session_state.start_app:
        logger.info("Application Starting Condition passed")
        if (
            st.session_state.openai_api_key is not None
            and st.session_state.openai_api_key != ""
        ) or st.session_state.provider_select != "OpenAI":
            logger.info("OpenAI key Checking condition passed")
            if OpenAIFunctions.check_openai_api_key():
                logger.info("Inference Started")
                StreamlitFunctions.streamlit_print_messages()
                StreamlitFunctions.streamlit_invoke_model()
            else:
                StreamlitFunctions.reset_history()
        else:
            with st.chat_message("assistant"):
                st.markdown("**'OpenAI API key'** is missing.")


if __name__ == "__main__":
    main()
