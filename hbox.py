import pygame
from container import *
from grid import *

class hbox(container):
	padding = 0

	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)
		container.__init__(self)

	def add(self, elem):
		container.add(self, elem)
		padding = self.padding
		if len(self.child_elements)-1 < 1:
			padding = 0
		elem.move(self.rect.w + padding, 0)
		if elem.rect.h > self.rect.h:
			self.resize(self.rect.w, elem.rect.h)
		self.resize(self.rect.w + elem.rect.w + padding, elem.rect.h)
		if len(self.child_elements) > 1:
			self.focus_grid.add_right(elem.get_focus_grid())
		else:
			self.focus_grid = elem.get_focus_grid()

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
			return self.parent.element_right(self.id)
		else:
			return self.parent.element_right(self.id)

	def get_focus_grid(self):
		new_grid = grid()
		for x in range(self.focus_grid.w):
			new_col = []
			old_col = self.focus_grid.get_col(x)
			for item in old_col:
				if item != None:
					new_col.append(item)
			if len(new_col) < self.focus_grid.h:
				repeat = self.focus_grid.h / len(new_col)
				tmp = []
				for i in new_col:
					for r in range(repeat):
						tmp.append(i)
				for i in range(self.focus_grid.h%len(new_col)):
					tmp.append(new_col[-1])
				new_col = tmp
			for i in range(len(new_col)):
				new_grid.set(x, i, new_col[i])
		return new_grid