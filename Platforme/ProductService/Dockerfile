FROM python:3.7

WORKDIR /productservice

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY /app/ ./app/

EXPOSE 8080

CMD [ "uvicorn" , "app.main:app" ,"--host","0.0.0.0" ,"--port" , "8080"]