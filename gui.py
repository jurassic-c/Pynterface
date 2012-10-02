class gui:
	child_elements = None
	surface = None

	def __init__(self, surface):
		self.child_elements = []
		self.surface = surface

	def draw(self, events):
		for child in self.child_elements:
			child.draw(events)

	def add(self, element):
		self.child_elements.append(element)
		element.set_gui(self)