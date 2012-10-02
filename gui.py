class gui:
	child_elements = None
	elements = None
	surface = None
	focus_id = None

	def __init__(self, surface):
		self.child_elements = []
		self.elements = []
		self.surface = surface
		self.focus = []

	def draw(self, events):
		for child in self.child_elements:
			child.draw(events)

	def add(self, elem):
		self.child_elements.append(elem)
		elem.set_gui(self)

	def register_element(self, elem):
		self.elements.append(elem)
		return len(self.elements) -1

	def get_element(self, elem_id):
		return self.elements[elem_id]

	def set_focus(self, elem_id):
		if self.focus_id and elem_id != self.focus_id:
			self.elements[self.focus_id].blur()
		self.focus_id = elem_id