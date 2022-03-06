# Use python:3 as base image. This is a debian based image with python in it
FROM python:3.9-slim

# Our working directory is now /app. Imagine that we have navigated to this
# directory and every following action is executed here
WORKDIR /app

# Lets copy requirements.txt to our working directory in this case to /app/requirements.txt
COPY requirements.txt .

# Install requirements.txt with contains list about needed modules to run our app
RUN pip install -r requirements.txt

#Copy local directory to working directory /app
COPY . .

# By default use and expose port 81
EXPOSE 8080

#Expose env variable BACKEND_SERVER to our image
ENV BACKEND_SERVER $BACKEND_SERVER

CMD [ "python", "./main.py" ]