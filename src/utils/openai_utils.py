"""Module doc string"""

import openai
import streamlit as st
from openai import OpenAI

from .logs import log_execution_time, logger


class OpenAIFunctions:
    """Module doc string"""

    @log_execution_time
    @staticmethod
    def invoke_model():
        """_summary_"""
        logger.debug("OpenAI invoked")
        client = OpenAI(api_key=st.session_state.openai_api_key)
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                max_tokens=st.session_state["openai_maxtokens"],
                stream=True,
                stream_options={"include_usage": True},
            )

            def stream_data():
                for chunk in stream:
                    if chunk.choices != []:
                        word = chunk.choices[0].delta.content
                        if word is not None:
                            yield word
                    if chunk.usage is not None:
                        yield {
                            "completion_tokens": chunk.usage.completion_tokens,
                            "prompt_tokens": chunk.usage.prompt_tokens,
                            "total_tokens": chunk.usage.total_tokens,
                        }

            return st.write_stream(stream_data)

    @log_execution_time
    @staticmethod
    def check_openai_api_key():
        """_summary_"""
        logger.info("Checking OpenAI Key")
        try:
            client = OpenAI(api_key=st.session_state.openai_api_key)
            client.models.list()
            logger.debug("OpenAI key Working")
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
