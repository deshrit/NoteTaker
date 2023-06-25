FROM python:3.11.4-slim-bookworm

WORKDIR /dNoteTaker

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p vol && \
    useradd -M dnotetaker && \
    chown -R dnotetaker:dnotetaker vol && \
    chmod a+x startup.sh

CMD ["/dNoteTaker/startup.sh"]