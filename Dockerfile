# Base python docker image
FROM python:3.10.1-buster

# Import Code
ADD . /code

# Changing the directory
WORKDIR /code

# installing lib

RUN pip install flask

# Exposing the port
EXPOSE 5000

# Running python file
CMD python app.py