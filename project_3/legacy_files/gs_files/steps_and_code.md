Steps
1 - Spin up environment using week 13 docker compose file
docker-compose up -d

2 - Create topic using kafka
docker-compose exec kafka kafka-topics --create --topic events --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181

3 - Start flask api
docker-compose exec mids env FLASK_APP=/w205/project-3-gschweer84/new_game_api.py flask run --host 0.0.0.0

4 - Open terminal 2

5 - Generate events in terminal 2 - manually for now, but need to use Apache Bench
a. manual version
docker-compose exec mids curl http://localhost:5000/
docker-compose exec mids curl http://localhost:5000/purchase_a_sword
docker-compose exec mids curl http://localhost:5000/join_guild
docker-compose exec mids curl http://localhost:5000/slayed_dragon
docker-compose exec mids curl http://localhost:5000/took_damage
docker-compose exec mids curl http://localhost:5000/purchase_armor
docker-compose exec mids curl http://localhost:5000/attempt_daily_quest
b. Apache bench version
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/purchase_a_sword
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/join_guild
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/slayed_dragon
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/took_damage
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/purchase_armor
docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/attempt_daily_quest
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/purchase_a_sword
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/join_guild
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/slayed_dragon
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/took_damage
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/purchase_armor
docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/attempt_daily_quest
c. add while loop with Apache Bench - consider adding randomness
while true; do
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/purchase_a_sword
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/join_guild
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/slayed_dragon
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/took_damage
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/purchase_armor
        docker-compose exec mids ab -n 10 -H "Host: user1.comcast.com" http://localhost:5000/attempt_daily_quest
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/purchase_a_sword
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/join_guild
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/slayed_dragon
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/took_damage
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/purchase_armor
        docker-compose exec mids ab -n 10 -H "Host: user2.att.com" http://localhost:5000/attempt_daily_quest
    sleep 10
done

6 - Read events from Kafka in terminal 2
a. batch version
docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning -e
b. streaming version - removes -e to run continuously
docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning

7 - Run spark script file from terminal 2, i.e. running a job
Use write_swords_stream.py or filter_swords_stream.py file but add udf functions and munged events
See extract_events.py, separate_events.py, transform_events.py, filtered_writes.py, 
docker-compose exec spark spark-submit /w205/project-3-gschweer84/<file_name>.py
batch with no write to database
docker-compose exec spark spark-submit /w205/project-3-gschweer84/new_filter_events_batch.py
batch with write to database
docker-compose exec spark spark-submit /w205/project-3-gschweer84/new_write_hive_table.py

8 - Create table in HDFS using Hive, or incorporate directly in spark script (above) - see write_hive_table.py
df = spark.read.parquet('/tmp/purchases')
df.registerTempTable('purchases')
query = """
create external table purchase_events
  stored as parquet
  location '/tmp/purchase_events'
  as
  select * from purchases
"""
spark.sql(query)

9 - Query using Presto
docker-compose exec presto presto --server presto:8080 --catalog hive --schema default
a. show tables
presto:default> show tables;
b. describe table
presto:default> describe <table_name>;
c. query table
presto:default> select * from <table_name>;

10 - Query purchase table and other tables for business analysis

Notes
example from week 12 
@app.route("/purchase_a_knife")
def purchase_a_knife():
    purchase_knife_event = {'event_type': 'purchase_knife',
                            'description': 'very sharp knife'}
    log_to_kafka('events', purchase_knife_event)
    return "Knife Purchased!\n"
    
Ask Vinny about SSH content at the end of week 12
