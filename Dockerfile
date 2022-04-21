FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /app/src
COPY simpleapp/ .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
