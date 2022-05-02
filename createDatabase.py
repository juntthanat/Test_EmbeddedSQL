import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE house
            (HNumber, HNAME, PRICE, CITY, FLOORSPACE)''')

# Insert a row of data
cur.execute("INSERT INTO house VALUES (1, 'Cronswell', 30000, 'Vienna', 40.61)")
cur.execute("INSERT INTO house VALUES (2, 'The Lodge', 80000, 'Minsk', 60.98)")
cur.execute("INSERT INTO house VALUES (3, 'Bakura', 6000, 'Kabul', 30.59)")
cur.execute("INSERT INTO house VALUES (4, 'Vientma', 50000, 'Manama', 60.47)")
cur.execute("INSERT INTO house VALUES (5, 'TreeTop', 100000, 'Paris', 80.58)")
cur.execute("INSERT INTO house VALUES (6, 'Bagarul', 8000, 'Banjul', 30.78)")
cur.execute("INSERT INTO house VALUES (7, 'Bagurs', 40000, 'Palikir', 50.43)")
cur.execute("INSERT INTO house VALUES (8, 'KingstonVille', 20000, 'Kingston', 20.80)")
cur.execute("INSERT INTO house VALUES (9, 'Luxem', 40000, 'Luxembourg', 50.18)")
cur.execute("INSERT INTO house VALUES (10, 'Maliki', 35000, 'Lilongwe', 30.52)")
cur.execute("INSERT INTO house VALUES (11, 'Bangkalou', 25000, 'Kuala Lumpur', 20.76)")
cur.execute("INSERT INTO house VALUES (12, 'MuscatVille', 40000, 'Muscat', 50.27)")
cur.execute("INSERT INTO house VALUES (13, 'Valet', 5000, 'Bangkok', 50.65)")
cur.execute("INSERT INTO house VALUES (14, 'Hamatsu', 70000, 'Tokyo', 25.56)")
cur.execute("INSERT INTO house VALUES (15, 'Kjuhe', 8500, 'Kigali', 20.89)")
cur.execute("INSERT INTO house VALUES (16, 'Asesa', 55000, 'Bucharest', 40.56)")
cur.execute("INSERT INTO house VALUES (17, 'Franel', 40000, 'Paris', 50.34)")
cur.execute("INSERT INTO house VALUES (18, 'Ulama', 15000, 'Vienna', 19.91)")
cur.execute("INSERT INTO house VALUES (19, 'Havillion', 60000, 'Singapore', 40.52)")
cur.execute("INSERT INTO house VALUES (20, 'Kumali', 20000, 'Manama', 30.15)")
cur.execute("INSERT INTO house VALUES (21, 'Khonbanrou', 40000, 'Bangkok', 40.89)")
cur.execute("INSERT INTO house VALUES (22, 'Ohari', 20000, 'Tokyo', 30.95)")
cur.execute("INSERT INTO house VALUES (23, 'Valets', 60000, 'Moscow', 100.5)")

# Save (commit) the changes
con.commit()
con.close()