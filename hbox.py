import pygame
from container import *

class hbox(container):
	padding = 0

	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)
		container.__init__(self)

	def add(self, elem):
		elem.move(self.rect.x + self.rect.w + self.padding*len(self.child_elements), self.rect.y)
		if elem.rect.h > self.rect.h:
			self.resize(self.rect.w, elem.rect.h)
		self.resize(self.rect.w + elem.rect.w, elem.rect.h)
		container.add(self, elem)

	def set_focus(self, element_id):
		container.set_focus(self, element_id)
		self.gui.h_focus_idx = self.focused_id

	def focus(self, options={}):
		if options.has_key("h_focus_idx"):
			options["child_id"] = options["h_focus_idx"]
		container.focus(self, options)

	def element_left(self, element_id):
		if len(self.child_elements):
			idx = self.child_ids[element_id]
			if idx > 0:
				return self.child_elements[idx-1]
			return self.child_elements[-1]
		else:
			return self.parent.element_right(self.id)

	def element_right(self, element_id):
		if len(self.child_elements):
			idx = self.child_ids[element_id]
			if idx < len(self.child_elements) -1:
				return self.child_elements[idx+1]
			return self.child_elements[0]
		else:
			return self.parent.element_right(self.id)