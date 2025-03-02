FROM python:3.7

WORKDIR /habitservice


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app/. /habitservice/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
