import csv
class Bike:
    def __init__(self,name,color,status):
        self.name = name
        self.color = color
        self.status = status
        
    def readBikes():
        print("Opna bikes.txt")
        with open('bikes.txt', 'r', newline='', encoding='utf-8')as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                bike = Bike(row[0],row[1],row[2])
                bikes.append(bike)
            print("Finished")
    
    def writeBikes():
        print("Skrifa í bikes.txt")
        file = None
        try:
            file = open("bikes.txt", "w", newline='', encoding="utf-8")
            for bike in bikes:
                line = ""
                line = bike.name + ";" + bike.color + ";" + bike.status + "\r\n"
                file.write(line)
        except IOError:
            print("An error occured trying to read this file")
        finally:
            print("Finished")
            if (file != None):
                file.close()
            print()
    
    def __str__(self):
        return f'Name: {self.name}\nColor: {self.color}\nStatus: {self.status}\n'
