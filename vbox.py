import pygame
from container import *

class vbox(container):
	padding = 0

	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)
		container.__init__(self)

	def add(self, elem):
		container.add(self, elem)
		padding = self.padding
		if len(self.child_elements)-1 < 1:
			padding = 0
		elem.move(0, self.rect.h + padding)
		if elem.rect.w > self.rect.w:
			self.resize(elem.rect.w, self.rect.h)
		self.resize(self.rect.w, elem.rect.h + self.rect.h + padding)
		if len(self.child_elements) > 1:
			self.focus_grid.add_bottom(elem.get_focus_grid())
		else:
			self.focus_grid = elem.get_focus_grid()

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

	def get_focus_grid(self):
		new_grid = grid()
		for y in range(self.focus_grid.h):
			new_row = []
			old_row = self.focus_grid.get_row(y)
			for item in old_row:
				if item != None:
					new_row.append(item)
			if len(new_row) < self.focus_grid.w:
				repeat = self.focus_grid.w / len(new_row)
				tmp = []
				for i in new_row:
					for r in range(repeat):
						tmp.append(i)
				for i in range(self.focus_grid.w%len(new_row)):
					tmp.append(new_row[-1])
				new_row = tmp
			for i in range(len(new_row)):
				new_grid.set(i, y, new_row[i])
		return new_grid