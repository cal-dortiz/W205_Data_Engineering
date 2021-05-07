import sqlite3

#define connection and cursor

connection = sqlite3.connect('take_damage.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
damage(enemy_id INTEGER PRIMARY KEY, name TEXT, damage INTEGER, event_type TEXT)"""

cursor.execute(command1)

# Add to Stores
cursor.execute("INSERT INTO damage VALUES (0, 'Claptrap C-137', 1, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (1, 'Dragon', 99, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (2, 'Mr. Meeseeks', 26, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (3, 'Bird Person', 41, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (4, 'Slimer', 56, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (5, 'John Wick', 67, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (6, 'Knight', 24, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (7, 'Tomato Person', 16, 'take_damage')")
cursor.execute("INSERT INTO damage VALUES (8, 'Tami', 57, 'take_damage')")


connection.commit()

# See Results For Debug Only
#cursor.execute("SELECT * FROM damage")

#results = cursor.fetchall()
#print(results)

connection.close()