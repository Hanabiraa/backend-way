#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

gunicorn service_1.asgi:app -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001 --chdir=/app