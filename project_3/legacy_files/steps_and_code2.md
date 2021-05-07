# Batch Steps

1 - Spin up environment using week 13 docker compose file
docker-compose up -d

2 - Create topic using kafka
docker-compose exec kafka kafka-topics --create --topic events --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181

3 - Start flask api
docker-compose exec mids env FLASK_APP=/<file path>/game_api.py flask run --host 0.0.0.0
docker-compose exec mids env FLASK_APP=/w205/group-project-repo/w205-project3/game_api.py flask run --host 0.0.0.0

4 - Open terminal 2

5 - Generate events in terminal 2

while true; do
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/join_a_guild/1
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/kill_enemy/2
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/take_damage/3
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/accepted_a_quest/1
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/transaction/1001
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/join_a_guild/1
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/kill_enemy/2
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/take_damage/3
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/accepted_a_quest/3
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/transaction/1001
    sleep 10
done

5.5 - open terminal 3 
    w205/group-project-repo/w205-project3

6 - Read events from Kafka in terminal 3
a. batch version
docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning -e

6.5 - open terminal 4
    
7 - Run spark script file from terminal 4, i.e. running a job
new batch with write to database
docker-compose exec spark spark-submit /<file path>/write_data_batch.py
docker-compose exec spark spark-submit /w205/group-project-repo/w205-project3/write_data_batch.py

8 - Query using Presto
docker-compose exec presto presto --server presto:8080 --catalog hive --schema default
a. show tables
presto:default> show tables;
b. describe table
presto:default> describe <table_name>;
c. query table
presto:default> select * from <table_name>;

9 - Query purchase table and other tables for business analysis

----
    
# Streaming Steps
    w205/group-project-repo/w205-project3
       
1 - Spin up environment using week 13 docker compose file
docker-compose up -d

2 - Create topic using kafka
docker-compose exec kafka kafka-topics --create --topic events --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181

3 - Start flask api
docker-compose exec mids env FLASK_APP=/<file path>/game_api.py flask run --host 0.0.0.0
docker-compose exec mids env FLASK_APP=/w205/group-project-repo/w205-project3/game_api.py flask run --host 0.0.0.0

4 - Open terminal 2

5 - Generate events in terminal 2

while true; do
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/join_a_guild/1
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/kill_enemy/2
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/take_damage/3
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/accepted_a_quest/1
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/transaction/1001
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/join_a_guild/1
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/kill_enemy/2
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/take_damage/3
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/accepted_a_quest/3
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/transaction/1001
    sleep 30
done

5.5 - open terminal 3 

6 - Read events from Kafka in terminal 3
b. streaming version - removes -e to run continuously
docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning

6.5 - open terminal 4

7 - Run spark script file from terminal 4, i.e. running a job
new stream
docker-compose exec spark spark-submit /<file path>/write_data_stream.py
docker-compose exec spark spark-submit /w205/group-project-repo/w205-project3/write_data_stream.py

7.5 - open terminal 5
    
8 - Create table in HDFS using Hive
for streaming follow these steps once to create tables
8.1 - navigate to same directory and run
docker-compose exec cloudera hive
8.2 - create tables
8.2.1 - this is failing
create external table if not exists default.transactions (Accept string, Host string, User_Agent string, event_type string, timestamp string, attributes array<struct< store_id: string, item_name: string, inventory_id: string, total_cost: string, category: string, on_hand_qty: string>>) stored as parquet location '/tmp/transactions'  tblproperties ("parquet.compress"="SNAPPY");
    
8.2.2
create external table if not exists default.transactions2 (Accept string, Host string, User_Agent string, event_type string, attributes string, store_id string, item_name string, inventory_id string, total_cost string, category string, on_hand_qty string, timestamp string) stored as parquet location '/tmp/transactions2'  tblproperties ("parquet.compress"="SNAPPY");
    
8.2.3
create external table if not exists default.transactions2 (Accept string, Host string, User_Agent string, event_type string, store_id string, item_name string, inventory_id string, total_cost string, category string, on_hand_qty string, timestamp string) row format serde 'org.apache.hadoop.hive.serde2.RegexSerDe' with serdeproperties ('input.regex'=".*:\"(.*?)\",\"attributes\":\\{\"store_id\":(\\w),\"item_name\":(\\w),\"inventory_id\":(\\w),\"total_cost\":(\\w),\"category\":(\\w),\"on_hand_qty\":(\\w).*$") 
stored as parquet location '/tmp/transactions2'  tblproperties ("parquet.compress"="SNAPPY");

example
CREATE  TABLE dd (key1 string, nestedKey1 string, nestedKey2 string) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' 
WITH SERDEPROPERTIES 
('input.regex'=".*:\"(.*?)\",\"key2\":\\{\"nestedKey1\":(\\d),\"nestedKey2\":(\\d).*$");

8.2.4
create external table if not exists default.transactions3 (Accept string, Host string, User_Agent string, event_type string, timestamp string, attributes string) stored as parquet location '/tmp/transactions3'  tblproperties ("parquet.compress"="SNAPPY");
    


open terminal 6

    
9 - Query using Presto
docker-compose exec presto presto --server presto:8080 --catalog hive --schema default
a. show tables
presto:default> show tables;
b. describe table
presto:default> describe <table_name>;
c. query table
presto:default> select * from <table_name>;

10 - Query purchase table and other tables for business analysis
    

other calls
    
docker-compose exec cloudera hadoop fs -ls /tmp/
    
docker-compose exec spark pyspark