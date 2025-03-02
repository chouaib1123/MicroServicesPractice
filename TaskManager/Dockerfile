FROM python:3.7


WORKDIR /taskservice


COPY requirement.txt requirement.txt


RUN pip install -r requirement.txt

COPY /app/ /taskservice/app

EXPOSE 8083

CMD [ "uvicorn" , "app.main:app" , "--host" , "0.0.0.0","--port","8083","--reload" ]