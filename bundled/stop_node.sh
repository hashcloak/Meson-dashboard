docker stack rm mixnet
while [ -n "`docker network ls --quiet --filter label=com.docker.stack.namespace=mixnet`" ]; do
  echo -n '.' && sleep 1
done
