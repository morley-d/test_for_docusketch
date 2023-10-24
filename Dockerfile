FROM python:3.10-slim

ENV PYTHONBUFFERED 1

COPY . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["flask_app.py"]
