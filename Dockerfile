# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

COPY src /app/src/

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]