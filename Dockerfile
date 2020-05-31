FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./requirements/pro.txt /code/
RUN pip install -r pro.txt
COPY . /code/
