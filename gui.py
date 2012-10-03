import pygame
from pygame.locals import *
from container import *
from keymap import *

elements = []
def get_id(elem):
	global elements
	elements.append(elem)
	return len(elements) -1

class gui(container):
	child_elements = None
	elements = None
	surface = None
	focus_id = None
	keymap = None

	def __init__(self, surface):
		container.__init__(self)
		self.surface = surface
		self.keymap = keymap()
		self.focus = []

	def draw(self, events):
		for child in self.child_elements:
			child.draw(events)
		for event in events:
			if event.type == KEYDOWN:
				if event.key == self.keymap.tab:
					self.tab()

	def add(self, elem):
		global elements
		container.add(self, elem)
		elem.set_gui(self)
		elements[0].focus()

	def get_element(self, elem_id):
		global elements
		return elements[elem_id]

	def set_focus(self, elem_id):
		global elements
		if self.focus_id != None and elem_id != self.focus_id:
			elements[self.focus_id].blur()
		self.focus_id = elem_id

	def tab(self):
		global elements
		focused = elements[self.focus_id]
		next = focused.next_element()
		next.focus()

	def next_element(self):
		return None