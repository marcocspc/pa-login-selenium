FROM alpine:3.17.0

RUN apk update
RUN apk add chromium chromium-chromedriver python3 py3-pip dbus

RUN mkdir /app
ADD requirements.txt /app

RUN pip install -r /app/requirements.txt
RUN rm /app/requirements.txt

ADD pa-captive-script.py /app
ADD cmd.sh /app
RUN chmod +x /app/cmd.sh

CMD [ "/app/cmd.sh" ]
