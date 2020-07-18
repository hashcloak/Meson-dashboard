if [[ $(docker info --format "{{.Swarm.LocalNodeState}}") != "active" ]]; then
  docker swarm init
fi

docker stack deploy -c bundle.yml mixnet
