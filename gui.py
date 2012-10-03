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
	shift = False
	ctrl = False
	alt = False

	h_focus_idx = 0
	v_focus_idx = 0

	def __init__(self, surface):
		container.__init__(self)
		self.surface = surface
		self.keymap = keymap()
		self.focus = []

	def draw(self, events):
		for child in self.child_elements:
			child.draw(events)
		for event in events:
			if event.type == KEYUP:
				if event.key in [K_LSHIFT, K_RSHIFT]:
					self.shift = False
				if event.key in [K_LCTRL, K_RCTRL]:
					self.ctrl = False
				if event.key in [K_LALT, K_RALT]:
					self.alt = False
			elif event.type == KEYDOWN:
				if event.key in [K_LSHIFT, K_RSHIFT]:
					self.shift = True
				if event.key in [K_LCTRL, K_RCTRL]:
					self.ctrl = True
				if event.key in [K_LALT, K_RALT]:
					self.alt = True
				if event.key == self.keymap.right:
					self.tab_right()
				elif event.key == self.keymap.left:
					self.tab_left()
				elif event.key == self.keymap.up:
					self.tab_up()
				elif event.key == self.keymap.down:
					self.tab_down()

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

	def tab(self, next_element, options={}):
		next_element.focus(options)

	def tab_right(self):
		global elements
		focused = elements[self.focus_id]
		right = focused.element_right()
		self.tab(right, {"v_focus_idx": self.v_focus_idx})

	def tab_left(self):
		global elements
		focused = elements[self.focus_id]
		left = focused.element_left()
		self.tab(left, {"v_focus_idx": self.v_focus_idx})

	def tab_up(self):
		if self.focus_id == None:
			return
		global elements
		focused = elements[self.focus_id]
		above = focused.element_above()
		self.tab(above, {"h_focus_idx": self.h_focus_idx})

	def tab_down(self):
		if self.focus_id == None:
			return
		global elements
		focused = elements[self.focus_id]
		below = focused.element_below()
		self.tab(below, {"h_focus_idx": self.h_focus_idx})

	def next_element(self):
		return None

	def prev_element(self):
		return None

	def element_above(self):
		return None