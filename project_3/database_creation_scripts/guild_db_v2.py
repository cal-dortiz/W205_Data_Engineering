import sqlite3

#define connection and cursor

connection = sqlite3.connect('guild.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
guild(guild_id INTEGER PRIMARY KEY, name TEXT, event_type TEXT)"""

cursor.execute(command1)

# Add to Stores
cursor.execute("INSERT INTO guild VALUES (0, 'Archespace Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (1, 'Fighters Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (2, 'Mages Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (3, 'Thieves Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (4, 'Data Wranglers Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (5, 'Traders Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (6, 'Assassins Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (7, 'Knights Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (8, 'Tech-Knights Templars', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (9, 'Data Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (10, 'Data Warriors', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (11, 'Ninja Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (12, 'Kafka Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (13, 'Spark Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (14, 'Mongo Warriors', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (15, 'GingerBread Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (16, 'Incredible-Knight Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (17, 'Brave Slayers', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (18, 'Funny Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (19, 'Captain Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (20, 'Dreadful-Knights Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (21, 'Presto-Knights Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (22, 'Py Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (23, 'Thunder Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (24, 'Invasion-Knights Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (25, 'Rescue Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (26, 'Legends Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (27, 'Rivals-Knight Templar', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (28, 'Crystalhunt Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (29, 'Blast Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (30, 'Blockflight Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (31, 'Science Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (32, 'Borderlust Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (33, 'Android Warfare Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (34, 'Eternal Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (35, 'Everforce Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (36, 'Astroside Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (37, 'Archepoint Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (38, 'Cyberlight Guild', 'join_a_guild')")
cursor.execute("INSERT INTO guild VALUES (39, 'Brutalflight Guild', 'join_a_guild')")

connection.commit()

# See Results for debug only
#cursor.execute("SELECT * FROM inventory")

#results = cursor.fetchall()
#print(results)

connection.close()