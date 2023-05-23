# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /portfolio

COPY portfolio/requirements.txt /requirements.txt

RUN pip3 install -r portfolio/requirements.txt

COPY . .
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

