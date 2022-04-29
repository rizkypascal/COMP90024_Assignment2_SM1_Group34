# Mount volumes
sudo mkfs.ext4 /dev/vdb 
sudo mkdir -p /mnt/couchdb
sudo mount /dev/vdb /mnt/couchdb -t auto
sudo chown ubuntu /mnt/couchdb
sudo chmod 775 /mnt/couchdb/data/

# install docker 
sudo apt install docker.io

# Add user to docker group 
sudo usermod -aG docker $USER

export declare -a nodes=(172.26.130.122 172.26.129.21 172.26.133.246)

# export node='172.26.130.122'
# export name='master'
# export node='172.26.129.21'
# export name='worker1'
# export node='172.26.133.246'
# export name='worker2'

export masternode='172.26.130.122'
export size=${#nodes[@]}
export user='admin'
export pass='team34'
export VERSION='3.2.1'
export cookie='xxxteam34xxx'

# continue CouchDB
docker pull ibmcom/couchdb3:${VERSION}


for node in "${nodes[@]}" 
  do
    if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ] 
       then
         docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet) 
         docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
    fi 
done


docker create\
    --name couchdb${name}\
    --env COUCHDB_USER=${user}\
    --env COUCHDB_PASSWORD=${pass}\
    --env COUCHDB_SECRET=${cookie}\
    --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\" -kernel inet_dist_listen_min 9100 -kernel inet_dist_listen_max 9100"\
    -p 5984:5984\
    -p 9100:9100\
    -p 4369:4369\
    -v /mnt/couchdb/data:/opt/couchdb/data\
    ibmcom/couchdb3:${VERSION}


# Start the containers (and wait a bit while they boot):

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' '`)
for cont in "${conts[@]}"; do docker start ${cont}; done

# Set up the CouchDB cluster:


curl -XPOST "http://${user}:${pass}@127.0.0.1:5984/_cluster_setup" \
      --header "Content-Type: application/json"\
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
             \"username\": \"${user}\", \"password\":\"${pass}\",\"node_count\": ${size}}"


curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json"\
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
             \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": 5984,\
             \"node_count\": \"${size}\", \"remote_node\": \"${node}\",\
             \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"


curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json"\
    --data "{\"action\": \"add_node\", \"host\":\"${node}\",\
            \"port\": 5984, \"username\": \"${user}\", \"password\":\"${pass}\"}"

curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"

curl -XPOST "http://${user}:${pass}@127.0.0.1:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"


# check status
curl "http://${user}:${pass}@${masternode}:5984/_cluster_setup"

curl "http://${user}:${pass}@${masternode}:5984/_membership"

curl "http://${user}:${pass}@${node}:5984/_membership"
