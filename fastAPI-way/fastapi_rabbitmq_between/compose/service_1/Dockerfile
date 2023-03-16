FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# update packages
RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y telnet netcat \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# create user
RUN addgroup --system service_1 \
    && adduser --system --ingroup service_1 service_1

# Requirements are installed here to ensure they will be cached.
RUN pip install poetry
COPY ./service_1/pyproject.toml pyproject.toml
RUN poetry export --without-hashes --output=/requirements.txt
RUN pip install -r /requirements.txt

# copy entrypoint scripts
COPY ./compose/service_1/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown service_1 /entrypoint.sh

COPY ./compose/service_1/start.sh /start.sh
RUN chmod +x /start.sh
RUN chown service_1 /start.sh

# copy source
RUN mkdir app
WORKDIR /app
COPY ./service_1 ./service_1
RUN chown -R service_1:service_1 /app

USER service_1

ENTRYPOINT ["/entrypoint.sh"]
