from element import *

class container(element):
	child_elements = None

	def __init__(self):
		self.child_elements = []
		element.__init__(self)

	def add(self, elem):
		element.gui = self.gui
		self.child_elements.append(elem)

	def draw(self, events):
		for child in self.child_elements:
			child.draw(events)

	def set_gui(self, gui):
		element.set_gui(self, gui)
		for child in self.child_elements:
			child.set_gui(self.gui)

	def move(self, x, y):
		element.move(self, x, y)
		for child in self.child_elements:
			child.move(x+child.rect.x, y+child.rect.y)