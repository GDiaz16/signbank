FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY FinsSL-signbank/requirements.txt /code/
RUN pip install -r FinsSL-signbank/requirements.txt
COPY . /code/