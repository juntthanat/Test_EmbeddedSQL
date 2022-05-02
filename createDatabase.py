import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE house
            (HNumber, HNAME, PRICE, CITY, FLOORSPACE)''')

# Insert a row of data
cur.execute("INSERT INTO house VALUES (13, 'Valet', 5000, 'Bangkok', 50.65)")
cur.execute("INSERT INTO house VALUES (14, 'Hamatsu', 70000, 'Tokyo', 25.56)")
cur.execute("INSERT INTO house VALUES (17, 'Franel', 40000, 'Paris', 50.34)")
cur.execute("INSERT INTO house VALUES (19, 'Havillion', 60000, 'Singapore', 40.52)")
cur.execute("INSERT INTO house VALUES (23, 'Valets', 60000, 'Moscow', 100.5)")

# Save (commit) the changes
con.commit()
con.close()