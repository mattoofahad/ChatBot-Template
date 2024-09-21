---
title: This is a simple chat bot using openAI GPT models.
colorFrom: red
colorTo: green
emoji: 👾
sdk: streamlit
sdk_version: 1.31.1
app_file: app.py
pinned: false
---

# simple-chat-bot
This is a simple chat bot using openAI GPT models.

## Docker 
1. Create the docker container
    ```bash
    docker build -t streamlit .
    ```

2. run the container
    ```bash
    docker run -p 8501:8501 streamlit
    ```
3. The application is running on `http://localhost:8501/` URL.

## Create env

1. Create conda env
    ```bash
    conda create -n chat_bot_env python=3.10 -y
    ```

2. Activate env
    ```bash
    conda activate chat_bot_env
    ```

3. install packages
    ```bash
    pip install -r requirements.txt
    ```

## Run the application
1. start the application
    ```bash
    streamlit run app.py
    ```

# Local Action Commands

## Pylint
```bash
pylint src
```






