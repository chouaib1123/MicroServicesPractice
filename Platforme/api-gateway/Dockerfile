FROM python:3.7

WORKDIR /api-gateway

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY /app/ ./app/

EXPOSE 8081

CMD [ "uvicorn" , "app.main:app" , "--host","0.0.0.0", "--port" , "8081"]