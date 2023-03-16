#!/bin/bash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

rabbitmq_ready() {
    echo "Waiting for rabbitmq..."

    while ! nc -z rabbitmq 5672; do
      sleep 1
    done

    echo "rabbitmq started"
}

rabbitmq_ready

exec "$@"
