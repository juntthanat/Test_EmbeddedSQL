import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

cityName = str(input("please enter the city name: "))
temp = "Select * from house where city = \"" + cityName + "\" order by hnumber"
for row in cur.execute(temp):
    print(row)


con.close()