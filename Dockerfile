FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.port=8501", "--server.address=0.0.0.0"]
