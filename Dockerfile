FROM python:3.9.1
ADD . /dashboard-api
WORKDIR /dashboard-api
RUN pip install -r requirements.txt