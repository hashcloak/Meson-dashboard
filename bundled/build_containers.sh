docker pull grafana
docker pull prom/prometheus
docker pull hashcloak/meson:master
docker build -t local/nginx:latest -f nginx/Dockerfile nginx
