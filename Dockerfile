from alpine:latest
RUN apk add --no-cache py3-pip \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

ENV APP_ROOT=/app
RUN true \
    && chmod -R u+x ${APP_ROOT} \
    && chgrp -R 0 ${APP_ROOT} \
    && chmod -R g=u ${APP_ROOT} \
    && true

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["helloworld.py"]