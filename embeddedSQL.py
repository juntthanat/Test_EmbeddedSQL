import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM house ORDER BY PRICE'):
    print(row)

con.close()