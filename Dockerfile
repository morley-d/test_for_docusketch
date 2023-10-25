FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY flask_app.py .

CMD ["python", "flask_app.py"]
