FROM python:3.9.12-buster

RUN mkdir /app

ADD . /app 
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "-u", "search.py"]