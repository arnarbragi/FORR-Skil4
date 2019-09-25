import csv
class Clients:
	def __init__(self, kennitala, nafn, simanumer, netfang):
		self.kennitala = kennitala
		self.nafn = nafn
		self.simanumer = simanumer
		self.netfang = netfang
	def __str__(self):
		return "Kennitala: {}\n Nafn: {} \n Simanumer: \n Netfang {} \n"
	def newClients(self,kennitala,nafn,simanumer,netfang):
		kt = input("Sláðu inn kennitölu ")
		nafn = input("Sláðu inn nafn ")
		sima = input("Sláðu inn símanúmer ")
		netfang = input("Sláðu inn símanúmer")
		client = Clients(kt, nafn, sima, netfang)
		clientlist.append(client)
	def readclient():
			file = open("clients.txt", "r", newline="\r\n", encoding="utf-8")
			reader = csv.reader(file, delimiter=";")
			for row in reader:
				clit = Clients(row[0], row[1], row[2], row[3])
				clientlist.append(clit)
