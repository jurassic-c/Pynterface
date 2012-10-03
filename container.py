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

	def focus(self, options={}):
		if not len(self.child_elements):
			return
		if options.has_key("child_id"):
			self.focused_id = options["child_id"]
		if options.has_key("element_id"):
			self.focused_id = self.child_ids[options["element_id"]]
		if options.has_key("first_child"):
			self.focused_id = 0
		if options.has_key("last_child"):
			self.focused_id = -1
		self.child_elements[self.focused_id].focus(options)

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

	def next_child(self, elem_id):
		idx = self.child_ids[elem_id]
		if idx < len(self.child_elements) -1:
			return self.child_elements[idx+1]
		else:
			next = self.next_element()
			if next:
				return next
			return self.child_elements[0]

	def prev_child(self, elem_id):
		idx = self.child_ids[elem_id]
		if idx > 0:
			return self.child_elements[idx-1]
		else:
			prev = self.prev_element()
			if prev:
				return prev
			return self.child_elements[-1]

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