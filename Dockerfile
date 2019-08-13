FROM python:3.6-alpine

COPY . /usr/local/wxwork-webhook/
WORKDIR /usr/local/wxwork-webhook/
RUN pip install -r /usr/local/wxwork-webhook/requirements.txt && \
    chmod a+rx app.py
EXPOSE 5233

CMD ["app.py"]