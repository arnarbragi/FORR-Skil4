import csv
clientlist=[]
class Clients:
        def __init__(self, kennitala, nafn, simanumer, netfang):
                self.kennitala = kennitala
                self.nafn = nafn
                self.simanumer = simanumer
                self.netfang = netfang
        def __str__(self):
                return f"Kennitala: {self.kennitala}\n Nafn: {self.nafn} \n Simanumer: {self.simanumer}\n Netfang {self.netfang} \n"
        def newClient():
                kt = input("Sláðu inn kennitölu ")
                nafn = input("Sláðu inn nafn ")
                sima = input("Sláðu inn símanúmer ")
                netfang = input("Sláðu inn netfang ")
                client = Clients(kt, nafn, sima, netfang)
                clientlist.append(client)
        def readclient():
                file = open("clients.txt", "r", newline="\r\n", encoding="utf-8")
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                        clit = Clients(row[0], row[1], row[2], row[3])
                        clientlist.append(clit)
                print("Finished")
                return clientlist
        def writeClients():
                print("Skrifa í clients.txt")
                file = None
                try:
                        file = open("clients.txt", "w", newline='', encoding="utf-8")
                        for client in clientlist:
                                line = ""
                                line = client.kennitala + ";" + client.nafn + ";" + client.simanumer + ";" + client.netfang + "\r\n"
                                file.write(line)
                except IOError:
                        print("An error occured trying to read this file")
                finally:
                        print("Finished")
                        if (file != None):
                                file.close()
                        print()
