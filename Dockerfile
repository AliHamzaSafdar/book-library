FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update -y && \
    apt-get install -y netcat && \
    apt-get install -y binutils libproj-dev gdal-bin libgdal-dev


RUN pip install -r requirements.txt
RUN pip install daphne

COPY . /app/

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py test && python manage.py runserver 0.0.0.0:8000"]