FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Additional dependencies
  && apt-get install -y telnet netcat \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/local/fastapi/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/fastapi/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY ./compose/local/fastapi/celery/worker/start.sh /start-celeryworker.sh
RUN sed -i 's/\r$//g' /start-celeryworker.sh
RUN chmod +x /start-celeryworker.sh

COPY ./compose/local/fastapi/celery/beat/start.sh /start-celerybeat.sh
RUN sed -i 's/\r$//g' /start-celerybeat.sh
RUN chmod +x /start-celerybeat.sh

COPY ./compose/local/fastapi/celery/flower/start.sh /start-flower.sh
RUN sed -i 's/\r$//g' /start-flower.sh
RUN chmod +x /start-flower.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
