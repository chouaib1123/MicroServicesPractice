FROM python:3.7

WORKDIR /userService

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app/. /userService/app/

EXPOSE 8000

CMD [ "uvicorn" ,"app.main:app" ,"--host" ,"0.0.0.0" ,"--reload" ]