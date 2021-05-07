#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
import json
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import StructType, StructField, StringType


def purchase_sword_event_schema():
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
        StructField("sword_type", StringType(), True), 
        StructField("sword_cost", StringType(), True), 
        StructField("location", StringType(), True),
    ])


@udf('boolean')
def is_sword_purchase(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'purchase_sword':
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
        StructField("guild_type", StringType(), True),
    ])


@udf('boolean')
def is_guild_join(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'join_guild':
        return True
    return False


def slayed_dragon_event_schema():
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
        StructField("dragon_type", StringType(), True),
        StructField("location", StringType(), True),
        StructField("sword_type", StringType(), True),
    ])


@udf('boolean')
def is_dragon_slayed(event_as_json):
    """udf for filtering events
    """
    event = json.loads(event_as_json)
    if event['event_type'] == 'slayed_dragon':
        return True
    return False


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

    sword_purchases = raw_events \
        .filter(is_sword_purchase(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          purchase_sword_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_sword_purchases = sword_purchases \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_sword_purchases.printSchema()
    extracted_sword_purchases.show()

    extracted_sword_purchases.registerTempTable("extracted_sword_purchases")

    spark.sql("""
        create external table purchases
        stored as parquet
        location '/tmp/purchases'
        as
        select * from extracted_sword_purchases
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
    
    dragons_slayed = raw_events \
        .filter(is_dragon_slayed(raw_events.value.cast('string'))) \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          slayed_dragon_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')
    
    extracted_dragons_slayed = dragons_slayed \
        .rdd \
        .map(lambda r: Row(timestamp=r.timestamp, **json.loads(r.raw_event))) \
        .toDF()
    extracted_dragons_slayed.printSchema()
    extracted_dragons_slayed.show()

    extracted_dragons_slayed.registerTempTable("extracted_dragons_slayed")

    spark.sql("""
        create external table dragons_slayed
        stored as parquet
        location '/tmp/dragons_slayed'
        as
        select * from extracted_dragons_slayed
    """)
    
if __name__ == "__main__":
    main()
