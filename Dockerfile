FROM python:3.9.7-alpine

WORKDIR /meapi

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=12345

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 12345

CMD ["python", "app.py"]