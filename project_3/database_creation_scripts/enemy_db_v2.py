import sqlite3

#define connection and cursor

connection = sqlite3.connect('enemy.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
enemy(enemy_id INTEGER PRIMARY KEY, name TEXT, level INTEGER, event_type TEXT)"""

cursor.execute(command1)

# Add to Stores
cursor.execute("INSERT INTO enemy VALUES (0, 'Gus', 93, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (1, 'Mr. Meeseeks', 5, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (2, 'Dragon', 99, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (3, 'Private', 1, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (4, 'Nightwalker', 15, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (5, 'Elf', 7, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (6, 'Ronald McDonald', 36, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (7, 'Lex Luther', 47, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (8, 'Enemy Squire', 3, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (9, 'Sheep', 1, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (10, 'Velma', 45, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (11, 'Tito', 12, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (12, 'Adora', 35, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (13, 'Lannister', 97, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (14, 'Fons', 96, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (15, 'Em', 71, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (16, 'Giacopo', 56, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (17, 'Forrester', 87, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (18, 'Alexia', 90, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (19, 'Leoine', 10, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (20, 'Dino', 28, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (21, 'Wilma', 11, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (22, 'Ericha', 24, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (23, 'Tera', 71, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (24, 'Base', 72, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (25, 'Amos', 83, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (26, 'Reggy', 60, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (27, 'Drugi', 85, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (28, 'Dexter', 97, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (29, 'Querida', 27, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (30, 'Hardy', 19, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (31, 'Gunner', 4, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (32, 'Orelie', 4, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (33, 'Osborn', 76, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (34, 'Lorrin', 100, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (35, 'Gerianne', 49, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (36, 'Verla', 56, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (37, 'Gaspard', 73, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (38, 'Barclay', 53, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (39, 'Melinde', 13, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (40, 'Danit', 26, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (41, 'Thalia', 46, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (42, 'Saunders', 89, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (43, 'Dorothea', 42, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (44, 'Nikolos', 2, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (45, 'Corrie', 7, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (46, 'Adan', 52, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (47, 'Maureen', 9, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (48, 'Benedetta', 55, 'kill_enemy')")
cursor.execute("INSERT INTO enemy VALUES (49, 'Nona', 50, 'kill_enemy')")


connection.commit()

# See Results For Debug Only
#cursor.execute("SELECT * FROM enemy")

#results = cursor.fetchall()
#print(results)

connection.close()
