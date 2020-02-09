FROM python:3.7-slim as server

RUN apt-get update && \
    apt-get install -y git

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server/
RUN pip install -r requirements.txt

COPY ./server /server

RUN python manage.py collectstatic --noinput

#########################################

FROM nginx:1.17.2-alpine

RUN mkdir /nginx

RUN rm -v /etc/nginx/nginx.conf
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/ssl /etc/ssl/

COPY --from=server /server/staticfiles /nginx/static
