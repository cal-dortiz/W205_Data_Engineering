import sqlite3

#define connection and cursor

connection = sqlite3.connect('quest.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
quest(quest_id INTEGER PRIMARY KEY, name TEXT, contact TEXT)"""

cursor.execute(command1)

# Add to Stores

cursor.execute("INSERT INTO quest VALUES (0, 'There Is No Rule 10', 'Bevel Right')")
cursor.execute("INSERT INTO quest VALUES (1, 'Are We There, Yeti?', 'Sir Drexel of Yourn')")
cursor.execute("INSERT INTO quest VALUES (2, 'Chasing A-Me 01','Donald Whent')")
cursor.execute("INSERT INTO quest VALUES (3, 'TMission: Possible but Not Probable', 'Donald Whent')")
cursor.execute("INSERT INTO quest VALUES (4, 'Night Stalker Clean Up, Isle 2...', 'Bevel Left')")
cursor.execute("INSERT INTO quest VALUES (5, 'Of Coursers We Know', 'Veil of Symmetry')")
cursor.execute("INSERT INTO quest VALUES (6, 'Smelt On, Smelt Off', 'Teimo Kikukki')")
cursor.execute("INSERT INTO quest VALUES (7, 'What the Flux?', 'Teimo Kikukki')")
cursor.execute("INSERT INTO quest VALUES (8, 'You Are Fired', 'Reino Uonno')")
cursor.execute("INSERT INTO quest VALUES (9, 'There Is No Rule 6', 'Saejio Inahto')")
cursor.execute("INSERT INTO quest VALUES (10, 'What is going on?', 'Teimo Kikukki')")
cursor.execute("INSERT INTO quest VALUES (11, 'How much longer will this flux take?', 'Reino Uonno')")
cursor.execute("INSERT INTO quest VALUES (12, 'There is too much slaying and yapping', 'Veil of Symmetry')")
cursor.execute("INSERT INTO quest VALUES (13, 'What is the rush?', 'Sir Drexel of Yourn')")
cursor.execute("INSERT INTO quest VALUES (14, 'Lights not working, there might be possible..', 'Saejio Inahto')")

connection.commit()

# See Results for troubleshooting only
cursor.execute("SELECT * FROM quest")

results = cursor.fetchall()
print(results)

connection.close()
