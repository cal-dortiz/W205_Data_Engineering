#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword', 'sword_type': 'dagger', 'sword_cost': '100', 'location':'castle'}
    # reference: https://en.wikipedia.org/wiki/List_of_medieval_weapons
    # sword_type = ['dagger', 'rapier', 'saber']
    # sword_cost = ['100', '500', '1000']
    # location = ['castle', 'cave', 'barn']
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"


@app.route("/join_guild")
def join_guild():
    join_guild_event = {'event_type': 'join_guild', 'guild_type': 'apothecaries'}
    # reference: http://www.lordsandladies.org/medieval-london-guilds.htm
    # guild_type = ['apothecaries', 'blacksmiths', 'brewers']
    log_to_kafka('events', join_guild_event)
    return "Joined a guild!\n"


@app.route("/slayed_dragon")
def slayed_dragon():
    slayed_dragon_event = {'event_type': 'slayed_dragon', 'dragon_type': 'dragonnet', 'location': 'castle', 'sword_type': 'dagger'}
    # reference: https://dragons.fandom.com/wiki/Types_of_Dragons
    # dragon_type = ['dragonnet', 'hydra', 'drake']
    # location = ['castle', 'cave', 'barn']
    # sword_type = ['dagger', 'rapier', 'saber']
    log_to_kafka('events', slayed_dragon_event)
    return "Slayed a dragon!\n"


@app.route("/took_damage")
def took_damage():
    took_damage_event = {'event_type': 'took_damage', 'cause_damage': 'burns', 'damage_dealer': 'dragon', 'damage_level':'0.25'}
    # cause_damage = ['burns', 'wound', 'broken_bones']
    # damage_dealer = ['dragon', 'human', 'accident']
    # damage_level = [0.25, 0.5, 1.0]
    log_to_kafka('events', took_damage_event)
    return "Took damage!\n"


@app.route("/purchase_armor")
def purchase_armor():
    purchase_armor_event = {'event_type': 'purchase_armor', 'armor_type': 'chainmail', 'armor_cost': '500', 'location': 'barn'}
    # reference: https://en.wikipedia.org/wiki/Category:Medieval_armour
    # armor_type = ['chainmail', 'helmet', 'shield']
    # armor_cost = ['500', '1000', '2000']
    # location = ['castle', 'cave', 'barn']
    log_to_kafka('events', purchase_armor_event)
    return "Armor purchased!\n"


@app.route("/attempt_daily_quest")
def attempt_daily_quest():
    daily_quest_event = {'event_type': 'attempt_daily_quest', 'attempted': 'True'}
    # attempted = ['True', 'False']
    log_to_kafka('events', daily_quest_event)
    return "Daily quest attempted!\n"