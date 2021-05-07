import sqlite3

#define connection and cursor

connection = sqlite3.connect('take_damage.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
damage(enemy_id NTEGER PRIMARY KEY, name TEXT, damage INTEGER)"""

cursor.execute(command1)

# Add to Stores

cursor.execute("INSERT INTO damage VALUES (0, 'Claptrap C-137', '1')")
cursor.execute("INSERT INTO damage VALUES (1, 'Dragon', 99)")
cursor.execute("INSERT INTO damage VALUES (2, 'Mr. Meeseeks', 26)")
cursor.execute("INSERT INTO damage VALUES (3, 'Bird Person', 41)")
cursor.execute("INSERT INTO damage VALUES (4, 'Slimer', 56)")
cursor.execute("INSERT INTO damage VALUES (5, 'John Wick', 67)")
cursor.execute("INSERT INTO damage VALUES (6, 'Knight', 24)")
cursor.execute("INSERT INTO damage VALUES (7, 'Tomato Person', 16)")
cursor.execute("INSERT INTO damage VALUES (8, 'Tami', 57)")


connection.commit()

# See Results For Debug Only
cursor.execute("SELECT * FROM damage")

results = cursor.fetchall()
print(results)

connection.close()