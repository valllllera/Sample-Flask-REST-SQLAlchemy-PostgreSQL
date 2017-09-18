FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install psycopg2 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN python models.py

ENTRYPOINT ["python"]
CMD ["app.py"]