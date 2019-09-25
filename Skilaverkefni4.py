#Skilaverkefni 4
#Arnar og Jökull
import csv
from Bikes import Bike
from Clients import Clients

bikes=[]

Bike.readBikes()

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
    6. Exit
    """)
    val=input("Veldu 1-6: ")
    if val=="1":
        print()
        for bike in bikes:
            if bike.status == "available":
                print(bike)
    elif val=="2":
        pass
    elif val=="3":
        pass
    elif val=="4":
        pass
    elif val=="5":
        pass
    elif val=="6":
        print("Sjáumst seinna!")
        flag=False
    else:
        print("Þú verður að velja 1 til 6")


