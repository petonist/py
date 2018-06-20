import uuid
from matplotlib import pyplot as plt

class FloorElement:

	def __init__(self, name="noName", dimensions=(0,0), color="noColor", elementID="noID", elementType="noType", clickCoordinates=(0,0), elementCoordinates=(0,0)):
		self.name = name
		self.dimensions = dimensions
		self.color = color
		self.elementID = elementID
		self.elementType = elementType
		self.clickCoordinates = clickCoordinates
		self.elementCoordinates = elementCoordinates

	def drawElement(self):
		print("--- alustan joonistamist ---")
		print(f"nimi: {self.name}")
		print(f"mõõtmed: {self.dimensions}")
		print(f"värv: {self.color}")
		print(f"tüüp: {self.elementType}")

	def generateID(self):
		self.elementID = uuid.uuid4()
		print("ID:", self.elementID)
		print("--- joonistamine lõpetatud ---")

	def coordinateCheck(self):
		self.elementCoordinates = list(map(int, input("sisesta elemendi koordinaadid (xx:yy): ").split(":")))
		self.clickCoordinates = list(map(int, input("sisesta kliki koordinaadid (xx:yy): ").split(":")))

		if((((self.clickCoordinates[0] < self.elementCoordinates[0]) and (self.dimensions[0] + self.elementCoordinates[0] > self.clickCoordinates[0])) and 
		    ((self.clickCoordinates[1] < self.elementCoordinates[1]) and (self.dimensions[1] + self.elementCoordinates[1] > self.clickCoordinates[1]))) 
			or
		   (((self.clickCoordinates[0] > self.elementCoordinates[0]) and (self.dimensions[0] + self.elementCoordinates[0] < self.clickCoordinates[0])) and 
		    ((self.clickCoordinates[1] > self.elementCoordinates[1]) and (self.dimensions[1] + self.elementCoordinates[1] < self.clickCoordinates[1])))):
			print("klikk ei asu objektil")
		else:
			print("klikk asub elemendil ->", self.name)

	def export(self):
		x = [self.clickCoordinates[0], self.clickCoordinates[1], self.elementCoordinates[0], self.elementCoordinates[1]]
		y = [self.clickCoordinates[0], self.clickCoordinates[1], self.dimensions[0], self.dimensions[1]]
		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('xx:yy koordinaatide graaf')
		plt.plot(x, y)
		plt.show()
		#elemendi mõõtmeid ei võta arvesse joonistamisel

elements = [
	FloorElement(name="väike p6randa tykk", dimensions=(10,10), color="sinine", elementType="img"),
	FloorElement(name="keskmine p6randa tykk", dimensions=(20,30), color="punane", elementType="txt"),
	FloorElement(name="suur p6randa tykk", dimensions=(60,50), color="l2bipaistev", elementType="sym")
]

for element in elements:
	element.drawElement()
	element.generateID()
	element.coordinateCheck()
	element.export()
