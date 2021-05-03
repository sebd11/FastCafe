FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app ./app

CMD uvicorn --host=0.0.0.0 app.main:app --reload
