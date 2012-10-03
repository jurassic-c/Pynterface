from element import *
import gui

class container(element):
	child_elements = None
	child_ids = None
	focused_id = 0

	def __init__(self):
		self.child_elements = []
		self.child_ids = {}
		element.__init__(self)

	def add(self, elem):
		elem.parent = self
		elem.id = gui.get_id(elem)
		self.child_elements.append(elem)
		self.child_ids[elem.id] = len(self.child_elements)-1

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

	def focus(self):
		self.child_elements[self.focused_id].focus()

	def blur(self):
		self.child_elements[self.focused_id].blur()

	def next_child(self, elem_id):
		idx = self.child_ids[elem_id]
		if idx < len(self.child_elements) -1:
			return self.child_elements[idx+1]
		else:
			next = self.next_element()
			if next:
				return next
			return self.child_elements[0]