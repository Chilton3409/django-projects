# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /portfolio
RUN git clone https://github.com/Chilton3409/django-projects.git
COPY portfolio/requirements.txt portfolio/requirements.txt

RUN pip3 install -r portfolio/requirements.txt


COPY . .

EXPOSE 8000

CMD ["python3", "portfolio/manage.py", "runserver", "0.0.0.0:8000"]

