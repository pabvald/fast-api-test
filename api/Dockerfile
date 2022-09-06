FROM python:3.9

WORKDIR /code

ADD requirements.txt /code/requirements.txt

RUN pip install --upgrade -r requirements.txt

EXPOSE 8080

COPY ./ /code

ENTRYPOINT python api/main.py