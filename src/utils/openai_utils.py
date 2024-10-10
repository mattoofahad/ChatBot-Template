"""Module doc string"""

import openai
import streamlit as st
from litellm import completion
from openai import OpenAI

from .logs import log_execution_time, logger


class OpenAIFunctions:
    """Module doc string"""

    @log_execution_time
    @staticmethod
    def invoke_model():
        """_summary_"""

        logger.debug("OpenAI invoked")
        with st.chat_message("assistant"):
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            comp_args = {}
            if st.session_state.provider_select == "OpenAI":
                comp_args["api_key"] = st.session_state.openai_api_key
                comp_args["model"] = st.session_state["openai_model"]
            elif st.session_state.provider_select == "lm-studio":
                comp_args["base_url"] = "http://localhost:1234/v1"
                comp_args["api_key"] = st.session_state.provider_select
                comp_args["model"] = "gpt-4o-mini"
            comp_args["messages"] = messages
            comp_args["max_tokens"] = st.session_state["openai_maxtokens"]
            comp_args["stream"] = True
            comp_args["stream_options"] = {"include_usage": True}

            stream = completion(**comp_args)

            def stream_data():
                for chunk in stream:
                    if chunk.choices != []:
                        word = chunk.choices[0].delta.content
                        if word is not None:
                            yield word
                    if hasattr(chunk, "usage"):
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
        if st.session_state.provider_select == "lm-studio":
            logger.info("Local Provider is Sekected")
            return True
        else:
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
