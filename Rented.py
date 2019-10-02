import csv
rentedlist=[]
class Rented:
    def __init__(self,nafn,timi,hjol):
        self.nafn = nafn
        self.timi = timi
        self.hjol = hjol
    def readRented():
        file = open("rented.txt", "r", newline="\r\n", encoding="utf-8")
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            clit = Rented(row[0], row[1], row[2])
            rentedlist.append(clit)
        return rentedlist
    def writeRented():
        print("Skrifa í Rented.txt")
        file = None
        try:
            file = open("rented.txt", "w", newline='', encoding="utf-8")
            for rented in rentedlist:
                line = ""
                line = rented.nafn + ";" + rented.timi + ";" + rented.hjol +"\r\n"
                file.write(line)
        except IOError:
            print("An error occured trying to read this file")
        finally:
            print("Finished")
            if (file != None):
                file.close()
            print()
