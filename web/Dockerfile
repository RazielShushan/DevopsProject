FROM python:latest
COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x ./scripts/run.sh

EXPOSE 80

CMD ["/scripts/run.sh"]