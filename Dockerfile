FROM python:3-alpine
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >> "/etc/apk/repositories" \
    && apk update \
    && apk add rclone

WORKDIR /app
COPY app /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "app.py"]