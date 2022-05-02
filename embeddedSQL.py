import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

print("All Houses")
for row in cur.execute('SELECT * FROM house ORDER BY PRICE'):
    print(row)

print("\nHouses that have price < 50000")
for row in cur.execute('select * from house where price < 50000'):
    print(row)

print("\nHouse that is in Bangkok")
for row in cur.execute('select * from house where city = "Bangkok"'):
    print(row)

print("\nHouses that have V as the first letter")
for row in cur.execute('select * from house where hname like "V%" order by price'):
    print(row)

print("\nFloorspace Descending")
for row in cur.execute('select * from house order by floorspace desc'):
    print(row)

print("\nThe highest price")
for row in cur.execute('select * from house where price >= (select max(price) from house)'):
    print(row)

con.close()