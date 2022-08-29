FROM python:3.9.7-alpine

WORKDIR /meapi

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=12345

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY config.json config.json

COPY app.py app.py

COPY . .

EXPOSE 12345

CMD ["python", "app.py"]
