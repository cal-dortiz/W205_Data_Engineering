#!/bin/bash

# Spin up docker. This command uses the docker-compose tool to creat the containers and bridges for the following:
#

docker-compose up



# Create the assesment topic in Kafka on a single partition and single replication factor using zookeeper as the data
#broker
docker-compose exec kafka \
   kafka-topics \
     --create \
     --topic assessments \
     --partitions 1 \
     --replication-factor 1\
     --if-not-exists \
     --zookeeper zookeeper:32181
     
     
     
# Loads the json file from source    
curl -L -o assessment-attempts-20180128-121051-nested.json https://goo.gl/ME6hjp
     
  
  
# Kafka to create messages for each assessment submission
docker-compose exec mids \
    bash -c "cat /w205/project-2-cal-dortiz/assessment-attempts-20180128-121051-nested.json \
    | jq '.[]' -c \
    | kafkacat -P -b kafka:29092 -t assessments"\
        
        
        
# Launch Jupyter Notebook

docker-compose exec spark env PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port 8888 --ip 0.0.0.0 --allow-root --notebook-dir=/w205/' pyspark