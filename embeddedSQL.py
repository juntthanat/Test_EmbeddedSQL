import sqlite3

con = sqlite3.connect('buyAHouse.db')
cur = con.cursor()

def selection1():
    # All Houses
    for row in cur.execute('SELECT * FROM house ORDER BY hnumber'):
        print(row)

def selection2():
    userInput = int(input("\n1.) Highest Price \n2.) Lowest Price \n3.) More Than or equal to \n4.) Less Than or equal to\nSelection: "))
    if(userInput == 1):
        # The Highest Price
        for row in cur.execute('select * from house where price >= (select max(price) from house)'):
            print(row)
    elif(userInput == 2):
        # The Lowest Price
        for row in cur.execute('select * from house where price <= (select min(price) from house)'):
            print(row)
    elif(userInput == 3):
        inputPrice = str(input("Input the Price: "))
        temp = "select * from house where price >= " + inputPrice
        for row in cur.execute(temp):
            print(row)
    elif(userInput == 4):
        inputPrice = str(input("Input the Price: "))
        temp = "select * from house where price <= " + inputPrice
        for row in cur.execute(temp):
            print(row)
    else:
        print("Unknown Input Please Try again")
        exit()

def selection3():
    userInput = int(input("\n1.) Biggest FloorSpace \n2.) Smallest FloorSpace \n3.) More Than or equal to \n4.) Less Than or equal to\nSelection: "))
    if(userInput == 1):
        # The Biggest FloorSpace
        for row in cur.execute('select * from house where floorspace >= (select max(floorspace) from house)'):
            print(row)
    elif(userInput == 2):
        # The Smallest FloorSpace
        for row in cur.execute('select * from house where floorspace <= (select min(floorspace) from house)'):
            print(row)
    elif(userInput == 3):
        inputFloorSpace = str(input("Input the FloorSpace: "))
        temp = "select * from house where floorspace >= " + inputFloorSpace
        for row in cur.execute(temp):
            print(row)
    elif(userInput == 4):
        inputFloorSpace = str(input("Input the FloorSpace: "))
        temp = "select * from house where floorspace <= " + inputFloorSpace
        for row in cur.execute(temp):
            print(row)
    else:
        print("Unknown Input Please Try again")
        exit()

def selection4():
    userInput = int(input("\n1.) First Letter 2.) City Name\n Selection: "))
    if(userInput == 1):
        firstLetter = input("Please Enter the first letter of the city: ")
        if(len(firstLetter) == 1):
            temp = "Select * from house where city like \"" + firstLetter + "%\" order by hnumber"
            for row in cur.execute(temp):
                print(row)
        else: 
            print("There is more than one letter please try again")
            exit()
    elif(userInput == 2):
        cityName = str(input("please enter the city name(Please Capitalize the first letter): "))
        temp = "Select * from house where city = \"" + cityName + "\" order by hnumber"
        for row in cur.execute(temp):
            print(row)

while True:
    selection = int(input("\n\n1.) All House \n2.) Price of the House \n3.) The FloorSpace \n4.) Name of the city\n0.) Exit\nSelection: "))

    if(selection == 1):
        selection1()
    elif(selection == 2):
        selection2()
    elif(selection == 3):
        selection3()
    elif(selection == 4):
        selection4()
    else: break

con.close()