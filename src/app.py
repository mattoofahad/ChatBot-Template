"""Module doc string"""

import streamlit as st
from openai import OpenAI

from utils import (
    OpenAIFunctions,
    StreamlitFunctions,
    discord_hook,
    ConstantVariables,
    logger,
)

discord_hook("Simple chat bot initiated")


def main():
    """_summary_"""

    StreamlitFunctions.streamlit_page_config()
    StreamlitFunctions.streamlit_initialize_variables()

    if st.session_state.start_app:
        logger.info("Application Starting Condition passed")
        if (
            st.session_state.openai_api_key is not None
            and st.session_state.openai_api_key != ""
        ):
            logger.info("OpenAI key Checking condition passed")
            if OpenAIFunctions.check_openai_api_key():
                logger.info("Inference Started")
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
                StreamlitFunctions.reset_history()
        else:
            with st.chat_message("assistant"):
                st.markdown("**'OpenAI API key'** is missing.")

    with st.sidebar:
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


if __name__ == "__main__":
    main()
