import sqlite3

#define connection and cursor

connection = sqlite3.connect('guild.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
guild(guild_id INTEGER PRIMARY KEY, name TEXT)"""

cursor.execute(command1)

# Add to Stores

cursor.execute("INSERT INTO guild VALUES (0, 'Archespace Guild')")
cursor.execute("INSERT INTO guild VALUES (1, 'Fighters Guild')")
cursor.execute("INSERT INTO guild VALUES (2, 'Mages Guild')")
cursor.execute("INSERT INTO guild VALUES (3, 'Thieves Guild')")
cursor.execute("INSERT INTO guild VALUES (4, 'Data Wranglers Guild')")
cursor.execute("INSERT INTO guild VALUES (5, 'Traders Guild')")
cursor.execute("INSERT INTO guild VALUES (6, 'Assassins Guild')")
cursor.execute("INSERT INTO guild VALUES (7, 'Knights Templar')")
cursor.execute("INSERT INTO guild VALUES (8, 'Tech-Knights Templars')")
cursor.execute("INSERT INTO guild VALUES (9, 'Data Guild')")
cursor.execute("INSERT INTO guild VALUES (10, 'Data Warriors')")
cursor.execute("INSERT INTO guild VALUES (11, 'Ninja Templar')")
cursor.execute("INSERT INTO guild VALUES (12, 'Kafka Guild')")
cursor.execute("INSERT INTO guild VALUES (13, 'Spark Guild')")
cursor.execute("INSERT INTO guild VALUES (14, 'Mongo Warriors')")
cursor.execute("INSERT INTO guild VALUES (15, 'GingerBread Guild')")
cursor.execute("INSERT INTO guild VALUES (16, 'Incredible-Knight Templar')")
cursor.execute("INSERT INTO guild VALUES (17, 'Brave Slayers')")
cursor.execute("INSERT INTO guild VALUES (18, 'Funny Guild')")
cursor.execute("INSERT INTO guild VALUES (19, 'Captain Guild')")
cursor.execute("INSERT INTO guild VALUES (20, 'Dreadful-Knights Templar')")
cursor.execute("INSERT INTO guild VALUES (21, 'Presto-Knights Templar')")
cursor.execute("INSERT INTO guild VALUES (22, 'Py Guild')")
cursor.execute("INSERT INTO guild VALUES (23, 'Thunder Guild')")
cursor.execute("INSERT INTO guild VALUES (24, 'Invasion-Knights Templar')")
cursor.execute("INSERT INTO guild VALUES (25, 'Rescue Guild')")
cursor.execute("INSERT INTO guild VALUES (26, 'Legends Guild')")
cursor.execute("INSERT INTO guild VALUES (27, 'Rivals-Knight Templar')")
cursor.execute("INSERT INTO guild VALUES (28, 'Crystalhunt Guild')")
cursor.execute("INSERT INTO guild VALUES (29, 'Blast Guild')")
cursor.execute("INSERT INTO guild VALUES (30, 'Blockflight Guild')")
cursor.execute("INSERT INTO guild VALUES (31, 'Science Guild')")
cursor.execute("INSERT INTO guild VALUES (32, 'Borderlust Guild')")
cursor.execute("INSERT INTO guild VALUES (33, 'Android Warfare Guild')")
cursor.execute("INSERT INTO guild VALUES (34, 'Eternal Guild')")
cursor.execute("INSERT INTO guild VALUES (35, 'Everforce Guild')")
cursor.execute("INSERT INTO guild VALUES (36, 'Astroside Guild')")
cursor.execute("INSERT INTO guild VALUES (37, 'Archepoint Guild')")
cursor.execute("INSERT INTO guild VALUES (38, 'Cyberlight Guild')")
cursor.execute("INSERT INTO guild VALUES (39, 'Brutalflight Guild')")


connection.commit()

# See Results for debug only
cursor.execute("SELECT * FROM guild")

results = cursor.fetchall()
print(results)

connection.close()