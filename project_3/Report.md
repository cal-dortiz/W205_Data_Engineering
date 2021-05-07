# Project 3: Understanding User Behavior

## Report Analysis (through Presto CLI)

This report includes analysis of randomly-generated synthetic data that has been used to simulate real game and user events. Because the data is generated randomly, different results may be obtained when running the queries reflected below.

*1. First we'll look at the tables in HDFS*

`show tables;`

|    Table     |
|--------------|
| enemy_kills  |
| guild_joins  |
| quests       |
| take_damage  |
| transactions |



*2. Next, let's understand the structure of each table.*

`describe enemy_kills;`

|   Column   |  Type   | Comment |
| ---------- | ------- | ------- | 
| raw_event  | varchar |         
| timestamp  | varchar |         
| accept     | varchar |         
| host       | varchar |         
| user_agent | varchar |         
| event_type | varchar |         
| enemy_id   | bigint  |         
| name       | varchar |         
| level      | integer |         


`describe quests;`

|   Column   |  Type   | Comment |
| ---------- | ------- | ------- | 
| raw_event  | varchar |         
| timestamp  | varchar |         
| accept     | varchar |         
| host       | varchar |         
| user_agent | varchar |         
| event_type | varchar |         
| quest_id   | bigint  |         
| name       | varchar |         
| contact    | varchar |         


`describe guild_joins;`

|   Column   |  Type   | Comment |
| ---------- | ------- | ------- | 
| raw_event  | varchar |         
| timestamp  | varchar |         
| accept     | varchar |         
| host       | varchar |         
| user_agent | varchar |         
| event_type | varchar |         
| guild_id   | bigint  |         
| name       | varchar |         


`describe transactions;`

|   Column     |  Type   | Comment |
| ------------ | ------- | ------  | 
| raw_event    | varchar |         
| timestamp    | varchar |         
| accept       | varchar |         
| host         | varchar |         
| user_agent   | varchar |         
| event_type   | varchar |         
| store_id     | bigint  |         
| item_name    | varchar |         
| inventory_id | bigint  |         
| total_cost   | double  |         
| category     | varchar |         
| on_hand_qty  | integer |         


`describe take_damage;`

|   Column   |  Type   | Comment |
| ---------- | ------- | ------- |
| raw_event  | varchar |         
| timestamp  | varchar |         
| accept     | varchar |         
| host       | varchar |         
| user_agent | varchar |         
| event_type | varchar |         
| enemy_id   | bigint  |         
| name       | varchar |         
| damage     | integer |         


*3. Here's some business questions that can be answered with this data:*

* 1. How many different guilds exist currently?

`select count(distinct name) as count_guild
from guild_joins;`

| count_guild |
| ----------- | 
|          26 |

* 2. How many guilds are called Templars?

`select count(distinct name) as count_guild_templar
from guild_joins
where name like '%Templar';`

| count_guild_templar | 
| ------------------- |
| 10                  |


* 3. What are the most common quests accepted?

`select name, count(name) as total_quests
from quests
group by name
order by count(name) desc;`

| name                                          | total_quests |
| --------------------------------------------- | ------------ |
| Are We There, Yeti?                           |            7 | 
| There Is No Rule 6                            |            7 |
| Of Coursers We Know                           |            7 |
| There is too much slaying and yapping         |            7 |
| You Are Fired                                 |            7 |


* 4. What are the least common contacts in quests?

`select contact, count(contact) as total_counts
from quests
group by contact
order by count(contact) desc;`

|      contact        | total_counts |
| ------------------- | ------------ |
| Bevel Right         |            4 |
| Bevel Left          |            4 |


* 5. What is average level of killing an enemy?

`select round(avg(level),2) as average_level
from enemy_kills;`

| average_level |
|---------------|
|         44.62 |


* 6. Which user was killed on the lowest level?

`select name, min(level) as low_level
from enemy_kills
group by name
order by min(level)
limit 2;`

|      name       | low_level |
| --------------- | --------- |
| Private         |         1 |
| Sheep           |         1 |



* 7. Which game level has had the highest amount of kills?

`select level, count(*) as total_kills
from enemy_kills
group by level
order by count(*) desc
limit 3;`

| level | total_kills |
| ----- | ----------- |
|   56  |          10 |
|     7 |           7 |
|     4 |           6 |


* 8. What is the costliest item?

`select item_name, max(total_cost) as highest_cost
from transactions
group by item_name
order by max(total_cost) desc;`

|  item_name   | highest_cost |
| ------------ | ------------ |
| Sacred Bow   |       1500.0 |
 

* 9. What is highest total cost of each category?

`select category, max(total_cost) as highest_cost
from transactions
group by category
order by max(total_cost) desc;`

| category | highest_cost |
| -------- | ------------ |
| Bow      |       1500.0 |
| Sword    |       1000.0 |
| Armor    |        500.0 |
 

* 10. What is the total value of items in each store?

`select store_id, sum(total_cost * on_hand_qty) as total_value
from transactions
group by store_id;`

| store_id | total_value |
| -------- | ----------- |
|        5 |    276500.0 |
|        1 |    175000.0 |
|        4 |    182000.0 |
|        2 |    248500.0 |
|        3 |    301000.0 |
        

* 11. How many items are in each category?

`select category, count(distinct item_name) as item_count_category
from transactions
group by category;`

| category | item_count_category |
| -------- | ------------------- |
| Bow      |                   1 |
| Armor    |                   1 |
| Sword    |                   1 |
 

* 12. How many items are in each store?*

`select store_id, count(distinct item_name) as item_count_store
from transactions
group by store_id;`

| store_id | item_count_store |
| -------- | ---------------- |
|        3 |                3 |
|        4 |                3 |
|        1 |                3 |
|        2 |                3 |
|        5 |                3 |


* 13. Who has taken the highest amount of damage?

`select name, max(damage) as highest_damage
from take_damage
group by name
order by max(damage) desc
limit 2;`

|   name    | highest_damage |
| --------- | -------------- |
| Dragon    |             99 |
| John Wick |             67 |
 

* 14. Which enemy has caused the highest damage?

`select enemy_id, max(damage) as highest_damage
from take_damage
group by enemy_id
order by max(damage) desc
limit 3;`


| enemy_id | highest_damage |
| -------- | -------------- |
|        1 |             99 |
|        5 |             67 |
|        8 |             57 |
        
