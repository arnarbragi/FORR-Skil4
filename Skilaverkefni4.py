#Skilaverkefni 4
#Arnar og Jökull
import csv
from Bikes import Bike
from Clients import Clients
from Rented import Rented

def innskraning():
    nyr=input("Ertu nýr viðskiptavinur?(ja/nei): ")
    if nyr == "ja":
        Clients.newClient()
        rettnafn=input("Sláðu inn nafn til að skrá þig inn: ")
        print("Velkominn aftur",rettnafn)
        print()
    elif nyr == "nei":
        til = False
        nafn=input("Hvað heitir þú? ")
        for client in clientlist:
            if client.nafn == nafn:
                til = True
                rettnafn = client.nafn
        if til:
            print("Velkominn aftur",rettnafn)
            print()
        else:
            print("Enginn er skráður undir þessu nafni")
    else:
        print("Þú verður að velja ja eða nei")
    return rettnafn

def leigja(basis):
    for bike in bikes:
        if bike.status == "available":
            print(bike)
    hjol=input("Hvaða hjól viltu leigja? ")
    til=False
    for bike in bikes:
        if bike.name == hjol and bike.status == "available":
            til=True
            rent = Rented(nafn,basis,hjol)
            rentedlist.append(rent)
            bike.status = "rented"
    if til:
        pass
    else:
        print("Þetta hjól er annaðhvort ekki til eða ekki laust. Endilega reynið aftur.")

bikes=Bike.readBikes()

clientlist=Clients.readclient()

rentedlist=Rented.readRented()

flag = True
while flag:
    val=""
    print("""
    ====== Bike Rental Shop ======
    1. Display available bikes
    2. Request a bike on hourly basis $5
    3. Request a bike on daily basis $20
    4. Request a bike on weekly basis $60
    5. Return a bike
    6. Save/Exit
    """)
    val=input("Veldu 1-6: ")
    if val=="1":
        print()
        for bike in bikes:
            if bike.status == "available":
                print(bike)
    elif val=="2":
        nafn = innskraning()
        basis="H"
        leigja(basis)
                
    elif val=="3":
        nafn = innskraning()
        basis="D"
        leigja(basis)
        
    elif val=="4":
        nafn = innskraning()
        basis="W"
        leigja(basis)
        
    elif val=="5":
        til=False
        nafn = innskraning()
        print("---------Hjól sem þú hefur í leigu---------")
        for x in rentedlist:
            if x.nafn == nafn:
                print(x.hjol)
                til=True
        print("-------------------------------------------")
        if til:
            hjol=input("Hvaða hjóli ertu að skila? ")
            for bike in bikes:
                if bike.name == hjol:
                    bike.status = "available"
                    for x in rentedlist:
                        if x.hjol == hjol:
                            rentedlist.remove(x)
        else:
            print("Þú ert ekki með neitt hjól í leigu")
    elif val=="6":
        print("Sjáumst seinna!")
        flag=False
        Bike.writeBikes(bikes)
        Clients.writeClients()
        Rented.writeRented()
    else:
        print("Þú verður að velja 1 til 6")


