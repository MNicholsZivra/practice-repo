class Node:
	def __init__(self, coordinates):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.z = coordinates[3]

class Edge:
	def __init__(self, start, stop):
		self.start = start
		self.stop = stop
		
class Wireframe:
	def __init__(self):
		self.nodes = []
		self.edges = []