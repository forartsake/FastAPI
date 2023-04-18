FROM python:3.10.6
ENV PYTHONUNBUFFERED=0
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/fastapi-docker
COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv


RUN pipenv install --system

RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime

COPY . .

EXPOSE 8001

RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh