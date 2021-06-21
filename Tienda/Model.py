from datetime import date

class Client:
	def __init__(self, name, ide):
		self.name = name
		self.ide = ide

	def getName(self):
		return self.name

	def getId(self):
		return self.ide

class Order:
	def __init__(self, client):
		self.datee = date.today()
		self.total = 0
		self.Products = []
		self.client = client

	def addProduct(self,object):
		self.Products.append(object)
		self.total = self.total + object.getValue()


	def generateOrder(self):
		print("/////////////////////////////////////////////")
		print("Nombre: " + self.client.getName())
		print("\nProducts\t Price")
		for product in self.Products:
			print(product.getName() + "\t" + str(product.getValue()))

		print("Total: " + str(self.total))
		print("\n\n///////////////////////////////////////////////////////")

class ControlProduct:
	"""docstring for ControlProduct"""
	def __init__(self, ICA, name, frecuency, value):
		self.ICA = ICA
		self.name = name
		self.frecuency = frecuency
		self.value = int(value)

	def getICA(self):
		return self.ICA

	def getName(self):
		return self.name

	def getFrecuency(self):
		return self.frecuency

	def getValue(self):
		return self.value

class PlagueControl(ControlProduct):
	def __init__(self, ICA, name, frecuency, value, lack):
		super().__init__(ICA, name, frecuency, value)
		self.lack = lack

	def getLack(self):
		return self.lack

class FertilizerControl(ControlProduct):
	def __init__(self, ICA, name, frecuency, value, appdate):
		super().__init__(ICA, name, frecuency, value)
		self.appdate = appdate


	def getAppdate(self):
		return self.appdate

class Antibiotic:
	"""docstring for Antibiotics"""
	def __init__(self, dose, name, type, value):
		self.dose = dose
		self.name = name
		self.type = type
		self.value = value

	def getDose(self):
		return self.dose

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getValue(self):
		return self.value

