FROM python:3.9

# set the working directory in the container
WORKDIR /app

COPY requirements.txt /app/requirements.txt

# server

RUN pip install --upgrade pip 
RUN pip install -r /app/requirements.txt

# copy the content of the local src directory to the working directory
COPY play/ .


ADD . .

# EXPOSE 8000

# creates docker image
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "deep.wsgi.application"]

# deploys app
CMD gunicorn play.wsgi:application --bind 0.0.0.0:$PORT