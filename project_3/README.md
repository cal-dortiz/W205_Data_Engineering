# Project 3: Game API
## W205
### Simran Bhatia, Dan Ortiz, Graham Schweer
### 12/6/2020

## Summary
As data scientists at a game development company, we are building our latest mobile game that has the following events:
   - Buy Assets
   - Join Guilds
   - Kill Enemies
   - Take Damage
   - Accept Quests

Each event has its respective metadata attributes. Randomly-generated synthetic data is used in this analysis to simulate real game and user events.  

This report will walk through how the end-to-end data pipeline was created for this game. 


## Interesting Findings

   - There are 26 active guilds that players can join. They are not mutually exclusive.
   - Private and Sheep are the lowest level enemies in the game with a level of 1
   - The Dragon enemy can inflict the most damage at 99


## How This Project is Structured

#### Pipeline
   - Docker-compose, Kafka producer and the API server is started with [Start API Server](start_api_server.sh)
   - API data is stored in the .db files [db folder](db)
   - Data in the .db files can be edited in the [db creation folder](database_creation_scripts)
   - Synthetic data is generated with [call_script](api_call_script.py)
   - Datafame schema and initial filtering is defined in [data_stream](write_data_stream_v3.py)
   - Tables in hive are built with the commands in the "How to Load" section 6 of this document

#### Analysis
   - Queries and results are located in [Report](Report.md)

## How to Load

### Setting up the Data pipeline
In terminal 1:

*1. Start shell script which will set up docker and run the API*

   - update the directory in line 14 of the 'start_api_server.sh' file 
   - run `sh start_api_server.sh`

In terminal 2:
(Make sure you're in the right directory.)

*2. Randomly generate events using Python script*

   - `python3 api_call_script.py`
    
In terminal 3:
(Make sure you're in the right directory.)

*3. Read generated events from Kafka, to run continuously in new stream*

   - `docker-compose exec mids kafkacat -C -b kafka:29092 -t events -o beginning`

In terminal 4: 
(Make sure you're in the right directory.)

*4. Run spark script file from, i.e. running a job*

   - `docker-compose exec spark spark-submit /<file path>/write_data_stream_v3.py`
   - remember to update the file path before running the script above


### Write data into HDFS/parquet files to make them available for analysis using Presto

In terminal 5:
(Make sure you're in the right directory.)

*5. Open Hive*:

   - `docker-compose exec cloudera hive`

*6. Create tables in Hive*:

**GUILD_JOINS**
```
create external table if not exists default.guild_joins 
(raw_event string, 
timestamp string, 
Accept string, 
Host string, 
User_Agent string, 
event_type string, 
guild_id bigint, 
name string) stored as parquet location '/tmp/guild_joins'  tblproperties ("parquet.compress"="SNAPPY");
```
    
**ENEMY_KILLS**

```
create external table if not exists default.enemy_kills (
raw_event string, 
timestamp string, 
Accept string, 
Host string, 
User_Agent string, 
event_type string, 
enemy_id bigint, 
name string, 
level smallint) stored as parquet location '/tmp/enemies_killed'  tblproperties ("parquet.compress"="SNAPPY");
```

**QUESTS**

```
create external table if not exists default.quests (
raw_event string, 
timestamp string, 
Accept string, 
Host string, 
User_Agent string, 
event_type string, 
quest_id bigint,
name string, 
contact string) stored as parquet location '/tmp/quest_accept'  tblproperties ("parquet.compress"="SNAPPY");
```

**TAKE_DAMAGE**
```
create external table if not exists default.take_damage (
raw_event string, 
timestamp string, 
Accept string, 
Host string, 
User_Agent string, 
event_type string, 
enemy_id bigint, 
name string, 
damage smallint) stored as parquet location '/tmp/damage_taken'  tblproperties ("parquet.compress"="SNAPPY");
```
    
**TRANSACTIONS**

```
create external table if not exists default.transactions (
raw_event string, 
timestamp string, 
Accept string, 
Host string, 
User_Agent string, 
event_type string, 
store_id bigint, 
item_name string, 
inventory_id bigint, 
total_cost float, 
category string, 
on_hand_qty smallint) 
stored as parquet location '/tmp/transactions'  
tblproperties ("parquet.compress"="SNAPPY");
```

### Set up Presto for analysis
In terminal 6:
(Make sure you're in the right directory.)

*7. Check if the tables exist in the HDFS tmp directory:*

   - `docker-compose exec cloudera hadoop fs -ls /tmp/`

*8. Start presto:*

   - `docker-compose exec presto presto --server presto:8080 --catalog hive --schema default`
   - query the data


## Technologies Used

   - Docker-compose: Used to manage the docker cluster. Must install the docker-compose app. (See Technologies Required)
   - Cloudera: Used to store files
   - Kafka: Used to generate messages\events into topic from the API calls
   - Zookeeper: Act as the data broker for Kafka
   - Spark: Used to build schema and filters by api call type
   - Hive: Construct data tables for analysis
   - Presto: Used to analyze data from Hive via Spark stream
   - Flask: Used to write the API to generate synthetic data
   - Linux Command Line: Used to execute all commands
   - Sql Lite: Used to structure database from which the API makes calls
   - Python: Used for multiple scripts in the project
   - Appache Bench: Used with the API to generate random synthetic data
 

## Technologies Required
In order to run this analysis you need to be running Linux (preferably Ubuntu Linux) and have docker downloaded and working.

   - Ubuntu: [Link to Ubuntu](https://ubuntu.com/)
   - Docker : [Link to Docker](https://www.docker.com/)
   - Docker-Compose:
      - On Linux, in the CLI run the following command: `sudo apt-get docker-compose`
      
## Technologies used in docker-compose file
The following packages will be downloaded and configured into their own containers during the first initialization of the start_api_server.sh shell. Therefore having Linux and docker installed on the machine is sufficient:

   - Kafka
   - Spark
   - Hive
   - Presto
   - Flask
   - MIDS (Includes Sql Lite, Python, CLI)
   - Apache Bench

