# Monitoring

## Metrics

As you're monitoring your Celery app, pay attention to the running metrics such as CPU and memory usage. If you're using Docker, make sure you check the running metrics for the containers as well as the host.

Let's look at a few open source and SaaS-based solutions.

Container Advisor
cAdvisor (Container Advisor) is an open source solution used for analyzing resource usage and performance data from running containers.

With your containers up and running, you can launch cAdvisor like so:

```sh
$ docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  gcr.io/cadvisor/cadvisor
```

> If you have trouble with the above command on Mac, try to add `--volume=/var/run/docker.sock:/var/run/docker.sock:ro \` and check [this Github issue](https://github.com/google/cadvisor/issues/1565).

script for docker-compose 

```dockerfile
cadvisor:
  image: gcr.io/cadvisor/cadvisor
  container_name: cadvisor
  volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:rw
    - /sys:/sys:ro
    - /var/lib/docker/:/var/lib/docker:ro
    - /var/run/docker.sock:/var/run/docker.sock:ro
```

## Prometheus

Next, let's take a look at another open source solution called Prometheus, which is used for event monitoring and alerting.

Prometheus can work in conjunction with cAdvisor by pulling the metrics data from it. You can then query the data directly from the Prometheus web UI. What's more, Prometheus also provides a powerful and flexible way to configure alerts based on specific events.

To use, add the two services to the docker-compose.prod.yml file:

```dockerfile
prometheus:
  image: prom/prometheus
  ports:
    - 9090:9090
  command:
    - --config.file=/etc/prometheus/prometheus.yml
  volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
  depends_on:
    - cadvisor

cadvisor:
  image: gcr.io/cadvisor/cadvisor
  container_name: cadvisor
  volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:rw
    - /sys:/sys:ro
    - /var/lib/docker/:/var/lib/docker:ro
    - /var/run/docker.sock:/var/run/docker.sock:ro
```

and prometheus.yml

```yaml
scrape_configs:

- job_name: cadvisor
  scrape_interval: 5s
  static_configs:
    - targets:
      - cadvisor:8080
```
