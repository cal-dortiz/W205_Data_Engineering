#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
import json
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import StructType, StructField, StringType


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
        StructField("attributes", StructType([
            StructField('enemy_id', StringType(), True),
            StructField('name', StringType(), True),
            StructField('level', StringType(), True)
        ]))])


@udf('boolean')
def is_enemy_killed(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'kill_enemy':
        return True
    return False


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
        StructField('attributes', StructType([
            StructField('guild_id', StringType(), True),
            StructField('name', StringType(), True)
        ]))])


@udf('boolean')
def is_guild_join(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'join_guild':
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
        StructField('attributes', StructType([
            StructField('enemy_id', StringType(), True),
            StructField('name', StringType(), True),
            StructField('damage', StringType(), True)
        ]))])


@udf('boolean')
def is_damage_taken(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'take_damage':
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
        StructField('attributes', StructType([
            StructField('quest_id', StringType(), True),
            StructField('name', StringType(), True),
            StructField('contact', StringType(), True)
        ]))])


@udf('boolean')
def is_quest_accepted(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'accept_quest':
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
        StructField('attributes', StructType([
            StructField('store_id', StringType(), True),
            StructField('item_name', StringType(), True),
            StructField('inventory_id', StringType(), True),
            StructField('total_cost', StringType(), True),
            StructField('category', StringType(), True),
            StructField('on_hand_qty', StringType(), True)
        ]))])


@udf('boolean')
def is_transaction(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'transaction':
        return True
    return False


# def slayed_dragon_event_schema():
#     """
#     root
#     |-- Accept: string (nullable = true)
#     |-- Host: string (nullable = true)
#     |-- User-Agent: string (nullable = true)
#     |-- event_type: string (nullable = true)
#     |-- timestamp: string (nullable = true)
#     """
#     return StructType([
#         StructField("Accept", StringType(), True),
#         StructField("Host", StringType(), True),
#         StructField("User-Agent", StringType(), True),
#         StructField("event_type", StringType(), True),
#         StructField("dragon_type", StringType(), True),
#         StructField("location", StringType(), True),
#         StructField("sword_type", StringType(), True),
#     ])


# @udf('boolean')
# def is_dragon_slayed(event_as_json):
#     """udf for filtering events
#     """
#     event = json.loads(event_as_json)
#     if event['event_type'] == 'slayed_dragon':
#         return True
#     return False


def main():
    """main
    """
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .enableHiveSupport() \
        .getOrCreate()

    raw_events = spark \
        .read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "events") \
        .option("startingOffsets", "earliest") \
        .option("endingOffsets", "latest") \
        .load()

#     purchase_events = raw_events \
#         .select(raw_events.value.cast('string').alias('raw'),
#                 raw_events.timestamp.cast('string')) \
#         .filter(is_purchase('raw'))

    transaction_records = raw_events \
        .filter(is_transaction(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          transaction_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_transactions = transaction_records \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_transactions.printSchema()
    extracted_transactions.show()

    extracted_transactions.registerTempTable("extracted_transactions")

    spark.sql("""
        create external table transactions
        stored as parquet
        location '/tmp/transactions'
        as
        select * from extracted_transactions
    """)

    guild_joins = raw_events \
        .filter(is_guild_join(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          join_guild_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_guild_joins = guild_joins \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_guild_joins.printSchema()
    extracted_guild_joins.show()

    extracted_guild_joins.registerTempTable("extracted_guild_joins")

    spark.sql("""
        create external table guild_joins
        stored as parquet
        location '/tmp/guild_joins'
        as
        select * from extracted_guild_joins
    """)
    
    enemies_killed = raw_events \
        .filter(is_enemy_killed(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          kill_enemy_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_enemy_kills = enemies_killed \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_enemy_kills.printSchema()
    extracted_enemy_kills.show()

    extracted_enemy_kills.registerTempTable("extracted_enemy_kills")

    spark.sql("""
        create external table enemies_killed
        stored as parquet
        location '/tmp/enemies_killed'
        as
        select * from extracted_enemy_kills
    """)
    
    damage_taken = raw_events \
        .filter(is_damage_taken(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          take_damage_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_take_damage = damage_taken \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_take_damage.printSchema()
    extracted_take_damage.show()

    extracted_take_damage.registerTempTable("extracted_damage_taken")

    spark.sql("""
        create external table damage_taken
        stored as parquet
        location '/tmp/damage_taken'
        as
        select * from extracted_damage_taken
    """)
    
    quest_accepted = raw_events \
        .filter(is_quest_accepted(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          accept_quest_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_quest_accept = quest_accepted \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_quest_accept.printSchema()
    extracted_quest_accept.show()

    extracted_quest_accept.registerTempTable("extracted_quests_accepted")

    spark.sql("""
        create external table quest_accept
        stored as parquet
        location '/tmp/quest_accept'
        as
        select * from extracted_quests_accepted
    """)
    
if __name__ == "__main__":
    main()
