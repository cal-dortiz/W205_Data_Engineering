import sqlite3

#define connection and cursor

connection = sqlite3.connect('enemy.db')

cursor = connection.cursor()

# Create store table

command1 = """CREATE TABLE IF NOT EXISTS
enemy(enemy_id INTEGER PRIMARY KEY, name TEXT, level INTEGER)"""

cursor.execute(command1)

# Add to Stores

cursor.execute("INSERT INTO enemy VALUES (0, 'Gus', 93)")
cursor.execute("INSERT INTO enemy VALUES (1, 'Mr. Meeseeks', 5)")
cursor.execute("INSERT INTO enemy VALUES (2, 'Dragon', 99)")
cursor.execute("INSERT INTO enemy VALUES (3, 'Private', 1)")
cursor.execute("INSERT INTO enemy VALUES (4, 'Nightwalker', 15)")
cursor.execute("INSERT INTO enemy VALUES (5, 'Elf', 7)")
cursor.execute("INSERT INTO enemy VALUES (6, 'Ronald McDonald', 36)")
cursor.execute("INSERT INTO enemy VALUES (7, 'Lex Luther', 47)")
cursor.execute("INSERT INTO enemy VALUES (8, 'Enemy Squire', 3)")
cursor.execute("INSERT INTO enemy VALUES (9, 'Sheep', 1)")
cursor.execute("INSERT INTO enemy VALUES (10, 'Velma', 45)")
cursor.execute("INSERT INTO enemy VALUES (11, 'Tito', 12)")
cursor.execute("INSERT INTO enemy VALUES (12, 'Adora', 35)")
cursor.execute("INSERT INTO enemy VALUES (13, 'Lannister', 97)")
cursor.execute("INSERT INTO enemy VALUES (14, 'Fons', 96)")
cursor.execute("INSERT INTO enemy VALUES (15, 'Em', 71)")
cursor.execute("INSERT INTO enemy VALUES (16, 'Giacopo', 56)")
cursor.execute("INSERT INTO enemy VALUES (17, 'Forrester', 87)")
cursor.execute("INSERT INTO enemy VALUES (18, 'Alexia', 90)")
cursor.execute("INSERT INTO enemy VALUES (19, 'Leoine', 10)")
cursor.execute("INSERT INTO enemy VALUES (20, 'Dino', 28)")
cursor.execute("INSERT INTO enemy VALUES (21, 'Wilma', 11)")
cursor.execute("INSERT INTO enemy VALUES (22, 'Ericha', 24)")
cursor.execute("INSERT INTO enemy VALUES (23, 'Tera', 71)")
cursor.execute("INSERT INTO enemy VALUES (24, 'Base', 72)")
cursor.execute("INSERT INTO enemy VALUES (25, 'Amos', 83)")
cursor.execute("INSERT INTO enemy VALUES (26, 'Reggy', 60)")
cursor.execute("INSERT INTO enemy VALUES (27, 'Drugi', 85)")
cursor.execute("INSERT INTO enemy VALUES (28, 'Dexter', 97)")
cursor.execute("INSERT INTO enemy VALUES (29, 'Querida', 27)")
cursor.execute("INSERT INTO enemy VALUES (30, 'Hardy', 19)")
cursor.execute("INSERT INTO enemy VALUES (31, 'Gunner', 4)")
cursor.execute("INSERT INTO enemy VALUES (32, 'Orelie', 4)")
cursor.execute("INSERT INTO enemy VALUES (33, 'Osborn', 76)")
cursor.execute("INSERT INTO enemy VALUES (34, 'Lorrin', 100)")
cursor.execute("INSERT INTO enemy VALUES (35, 'Gerianne', 49)")
cursor.execute("INSERT INTO enemy VALUES (36, 'Verla', 56)")
cursor.execute("INSERT INTO enemy VALUES (37, 'Gaspard', 73)")
cursor.execute("INSERT INTO enemy VALUES (38, 'Barclay', 53)")
cursor.execute("INSERT INTO enemy VALUES (39, 'Melinde', 13)")
cursor.execute("INSERT INTO enemy VALUES (40, 'Danit', 26)")
cursor.execute("INSERT INTO enemy VALUES (41, 'Thalia', 46)")
cursor.execute("INSERT INTO enemy VALUES (42, 'Saunders', 89)")
cursor.execute("INSERT INTO enemy VALUES (43, 'Dorothea', 42)")
cursor.execute("INSERT INTO enemy VALUES (44, 'Nikolos', 2)")
cursor.execute("INSERT INTO enemy VALUES (45, 'Corrie', 7)")
cursor.execute("INSERT INTO enemy VALUES (46, 'Adan', 52)")
cursor.execute("INSERT INTO enemy VALUES (47, 'Maureen', 9)")
cursor.execute("INSERT INTO enemy VALUES (48, 'Benedetta', 55)")
cursor.execute("INSERT INTO enemy VALUES (49, 'Nona', 50)")


connection.commit()

# See Results For Debug Only
cursor.execute("SELECT * FROM enemy")

results = cursor.fetchall()
print(results)

connection.close()
