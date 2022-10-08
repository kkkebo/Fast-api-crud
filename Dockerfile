FROM python:3.10.7-slim-buster
WORKDIR .
COPY requirements.txt .
RUN python3 -m pip install -r requirementsdeploy.txt
COPY . .
EXPOSE 8000
