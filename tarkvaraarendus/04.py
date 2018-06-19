import uuid

class FloorElement:
	name = ''
	dimensions = ''
	color = ''
	elementId = ''
	elementType = ''

	def __init__(self, name="noName", dimensions=(0,0), color="noColor", elementID="noID", elementType="noType"):
		self.name = name
		self.dimensions = dimensions
		self.color = color
		self.elementID = elementID
		self.elementType = elementType

	def drawElement(self):
		print("--- alustan joonistamist ---")
		print(f"olen: {self.name}")
		print(f"minu dimensioonid: {self.dimensions}")
		print(f"minu värv: {self.color}")
		print(f"olen: {self.elementType} tüüpi")

	def generateID(self):
		self.elementID = uuid.uuid4()
		print("minu ID:", self.elementID)
		print("--- joonistamine lõpetatud ---")

	def coordinateCheck(self):
		

	def export(self):
		pass

elements = [
	FloorElement(name="p6randa tykk", dimensions=(0,0), color="sinine", elementType="img"),
	FloorElement(name="mingi element", dimensions=(10,220), color="punane", elementType="txt"),
	FloorElement(name="ruut", dimensions=(50,90), color="l2bipaistev", elementType="sym")
]

for element in elements:
	element.drawElement()
	element.generateID()
