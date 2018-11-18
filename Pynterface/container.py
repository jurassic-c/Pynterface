from element import *
import gui
from grid import *

class container(element):
	child_elements = None
	child_ids = None
	focused_id = 0

	def __init__(self):
		self.child_elements = []
		self.child_ids = {}
		self.focus_grid = []
		element.__init__(self)
		self.focus_grid = grid()

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

	def set_target_surface(self, surface):
		element.set_target_surface(self, surface)
		for child in self.child_elements:
			child.set_target_surface(self.target_surface)

	def move(self, x, y):
		element.move(self, x, y)
		for child in self.child_elements:
			child.move(child.local_x, child.local_y)

	def focus(self, options={}):
		if not len(self.child_elements):
			return
		focused_id = self.focused_id
		if options.has_key("child_id"):
			focused_id = options["child_id"]
		if options.has_key("element_id"):
			focused_id = self.child_ids[options["element_id"]]
		if options.has_key("first_child"):
			focused_id = 0
		if options.has_key("last_child"):
			focused_id = -1
		if focused_id > len(self.child_elements) -1:
			focused_id = len(self.child_elements) -1
		self.child_elements[focused_id].focus(options)

	def set_focus(self, element_id):
		self.focused_id = self.child_ids[element_id]

	def blur(self):
		self.child_elements[self.focused_id].blur()

	def first_child(self):
		if len(self.child_elements):
			return self.child_elements[0]
		return None

	def last_child(self):
		if len(self.child_elements):
			return self.child_elements[-1]
		return None

	def element_right(self, elem_id):
		if self.parent:
			return self.parent.element_right(self.id)
		else:
			return None

	def element_left(self, elem_id):
		if self.parent:
			return self.parent.element_left(self.id)
		else:
			return None

	def element_above(self, element_id):
		if self.parent:
			return self.parent.element_above(self.id)
		else:
			return None

	def element_below(self, element_id):
		if self.parent:
			return self.parent.element_below(self.id)
		else:
			return None
