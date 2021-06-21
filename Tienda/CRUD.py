from Model import *


class Shop:
	def __init__(self):
		self.Clients = []
		self.Products = []
		self.Orders = []
		self.ActualOrder = None

	def addProductPlague(self, ICA, name, frecuency, value, lack):
		Product = PlagueControl(ICA, name, frecuency, value, lack)
		self.Products.append(Product)

	def addProductFertilizer(self, ICA, name, frecuency, value, appdate):
		Product = FertilizerControl(ICA, name, frecuency, value, appdate)
		self.Products.append(Product)

	def addAntibiotic(self, dose, name, typee, value):
		Product = Antibiotic(dose, name, typee, value)
		self.Products.append(Product)

	def newOrder(self):
		print("Inserte cedula: ")
		ide = input()
		client = None
		for person in self.Clients:
			if person.getId() == ide:
				client = person
		if client == None:
			print("Nuevo usuario. Por favor inserte su nombre: ")
			name = input()
			client = Client(name, ide)
			self.Clients.append(client)
		order = Order(client)
		return order

	def endOrder(self):
		self.ActualOrder.generateOrder()
		self.Orders.append(self.ActualOrder)

	def addToOrder(self):
		if self.ActualOrder == None:
			self.ActualOrder = self.newOrder()
			print("Usuario agregado.")
		print("///////////////////////////////////////////////////")
		for product in self.Products:
			print(product.getName())
		print("\n¿Qué producto desea (número en la lista)?")
		x = input()
		self.ActualOrder.addProduct(self.Products[int(x)-1])

	def currentOrder(self):
		if self.ActualOrder == None:
			return False
		else:
			return True
		



				

