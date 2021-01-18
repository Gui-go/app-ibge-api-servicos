# base image
FROM python:3.7

# adding requirements.txt to workdir
ADD requirements.txt .

# installing requirements
RUN pip install -r requirements.txt

# adding in all contents from flask_app folder into a new flask_app folder
COPY ./ ./

# exposing port 8000 on container
# EXPOSE 8000

# serving flask backend server
CMD [ "python", "app.py" ]