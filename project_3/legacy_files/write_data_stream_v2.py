#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import StructType, StructField, StringType


def join_guild_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("guild_id", StringType(), True),
        StructField("name", StringType(), True),
    ])


@udf('boolean')
def is_guild_join(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'join_a_guild':
        return True
    return False


def kill_enemy_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("enemy_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("level", StringType(), True),
        ])


@udf('boolean')
def is_enemy_killed(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'kill_enemy':
        return True
    return False


def accept_quest_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField('quest_id', StringType(), True),
        StructField('name', StringType(), True),
        StructField('contact', StringType(), True)
        ])


@udf('boolean')
def is_quest_accepted(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'accepted_a_quest':
        return True
    return False


def take_damage_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField('enemy_id', StringType(), True),
        StructField('name', StringType(), True),
        StructField('damage', StringType(), True)
        ])


@udf('boolean')
def is_damage_taken(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'take_damage':
        return True
    return False


def transaction_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField('store_id', StringType(), True),
        StructField('item_name', StringType(), True),
        StructField('inventory_id', StringType(), True),
        StructField('total_cost', StringType(), True),
        StructField('category', StringType(), True),
        StructField('on_hand_qty', StringType(), True)
        ])


@udf('boolean')
def is_transaction(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'transaction':
        return True
    return False



def main():
    """main
    """
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .getOrCreate()

    raw_events = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "events") \
        .load()

    enemies_killed = raw_events \
        .filter(is_enemy_killed(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          kill_enemy_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    sink_enemy_kills = enemies_killed \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_enemy_kills") \
        .option("path", "/tmp/enemies_killed") \
        .trigger(processingTime="10 seconds") \
        .start()

#     sink_enemy_kills.awaitTermination()
    
    guild_joins = raw_events \
        .filter(is_guild_join(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          join_guild_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')

    sink_guild_joins = guild_joins \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_guild_joins") \
        .option("path", "/tmp/guild_joins") \
        .trigger(processingTime="10 seconds") \
        .start()

#     sink_guild_joins.awaitTermination()
    
    quest_accepted = raw_events \
        .filter(is_quest_accepted(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          accept_quest_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    sink_accept_quest = quest_accepted \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_accept_quest") \
        .option("path", "/tmp/quest_accept") \
        .trigger(processingTime="10 seconds") \
        .start()

#     sink_accept_quest.awaitTermination()

    
    damage_taken = raw_events \
        .filter(is_damage_taken(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          take_damage_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    sink_take_damage = damage_taken \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_take_damage") \
        .option("path", "/tmp/damage_taken") \
        .trigger(processingTime="10 seconds") \
        .start()

#     sink_take_damage.awaitTermination()

    
    transaction_records = raw_events \
        .filter(is_transaction(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          transaction_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    sink_transactions = transaction_records \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_transactions") \
        .option("path", "/tmp/transactions") \
        .trigger(processingTime="10 seconds") \
        .start()

#     sink_transactions.awaitTermination()
    
    spark.streams.awaitAnyTermination()
    
if __name__ == "__main__":
    main()
