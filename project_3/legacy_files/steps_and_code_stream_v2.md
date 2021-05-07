# Streaming Steps
       
1 - Spin up environment using week 13 docker compose file
docker-compose up -d

2 - Create topic using kafka
docker-compose exec kafka kafka-topics --create --topic events --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181

3 - Start flask api
docker-compose exec mids env FLASK_APP=/<file path>/game_api_v2.py flask run --host 0.0.0.0

docker-compose exec mids env FLASK_APP=/w205/group-project-repo/w205-project3/game_api_v2.py flask run --host 0.0.0.0
    
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
    sleep 90
done

5.5 - open terminal 3 

6 - Read events from Kafka in terminal 3
b. streaming version - removes -e to run continuously
docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning

6.5 - open terminal 4

7 - Run spark script file from terminal 4, i.e. running a job
new stream
docker-compose exec spark spark-submit /<file path>/write_data_stream_v2.py

docker-compose exec spark spark-submit /w205/group-project-repo/w205-project3/write_data_stream_v2.py
    
   
7.5 - open terminal 5
    
8 - Create table in HDFS using Hive

8.1 - Run Hive
docker-compose exec cloudera hive

8.2 - create tables
GUILD_JOINS
create external table if not exists default.guild_joins (raw_event string, timestamp string, Accept string, Host string, User_Agent string, event_type string, guild_id string, name string) stored as parquet location '/tmp/guild_joins'  tblproperties ("parquet.compress"="SNAPPY");
    
ENEMY_KILLS
create external table if not exists default.enemy_kills (raw_event string, timestamp string, Accept string, Host string, User_Agent string, event_type string, enemy_id string, name string, level string) stored as parquet location '/tmp/enemies_killed'  tblproperties ("parquet.compress"="SNAPPY");

QUESTS
create external table if not exists default.quests (raw_event string, timestamp string, Accept string, Host string, User_Agent string, event_type string, quest_id string, name string, contact string) stored as parquet location '/tmp/quest_accept'  tblproperties ("parquet.compress"="SNAPPY");

TAKE_DAMAGE
create external table if not exists default.take_damage (raw_event string, timestamp string, Accept string, Host string, User_Agent string, event_type string, enemy_id string, name string, damage string) stored as parquet location '/tmp/damage_taken'  tblproperties ("parquet.compress"="SNAPPY");
    
TRANSACTIONS
create external table if not exists default.transactions (raw_event string, timestamp string, Accept string, Host string, User_Agent string, event_type string, store_id string, item_name string, inventory_id string, total_cost string, category string, on_hand_qty string) stored as parquet location '/tmp/transactions'  tblproperties ("parquet.compress"="SNAPPY");

8.5 - open terminal 6

9 - Query using Presto
docker-compose exec presto presto --server presto:8080 --catalog hive --schema default

a. show tables
presto:default> show tables;
b. describe table
presto:default> describe <table_name>;
c. query table
presto:default> select * from <table_name>;

10 - Query tables and other tables for business analysis
    
11 - other calls
    
docker-compose exec cloudera hadoop fs -ls /tmp/
    
docker-compose exec spark pyspark
    
w205/group-project-repo/w205-project3
    
    
