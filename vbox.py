import pygame
from container import *

class vbox(container):
	padding = 0

	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)
		container.__init__(self)

	def add(self, elem):
		elem.move(self.rect.x, self.rect.y + self.rect.h + self.padding*len(self.child_elements))
		if elem.rect.w > self.rect.w:
			self.resize(elem.rect.w, self.rect.h)
		self.resize(elem.rect.w, self.rect.h + elem.rect.h)
		container.add(self, elem)

	def focus(self, options={}):
		if options.has_key("v_focus_idx"):
			options["child_id"] = options["v_focus_idx"]
		container.focus(self, options)

	def element_above(self, element_id):
		if len(self.child_elements):
			idx = self.child_ids[element_id]
			if idx > 0:
				return self.child_elements[idx-1]
			return self.child_elements[-1]
		else:
			return self.parent.element_above(self.id)

	def element_below(self, element_id):
		if len(self.child_elements):
			idx = self.child_ids[element_id]
			if idx < len(self.child_elements) -1:
				return self.child_elements[idx+1]
			return self.child_elements[0]
		else:
			return self.parent.element_below(self.id)

	def set_focus(self, element_id):
		container.set_focus(self, element_id)
		self.gui.v_focus_idx = self.focused_id