import pygame
from pygame.locals import *
from container import *
from keymap import *
from events import *
from event_manager import *

elements = []
def get_id(elem):
	global elements
	elements.append(elem)
	return len(elements) -1

class gui(container):
	child_elements = None
	elements = None
	surface = None
	focus_coords = None
	keymap = None
	shift = False
	ctrl = False
	alt = False

	h_focus_idx = 0
	v_focus_idx = 0

	tabs = None
	tab_idx = 0

	frame_time = 0

	mouse_pos = None

	def __init__(self, surface):
		container.__init__(self)
		self.surface = surface
		self.rect = surface.get_rect()
		self.keymap = keymap()
		self.focus_coords = (0,0)
		self.tabs = []
		self.mouse_pos = (0,0)
		self.eventmgr.bind(MOUSEMOTION, self._on_mouse_motion)
		self.eventmgr.bind(KEYDOWN, self._on_keydown)
		self.eventmgr.bind(KEYUP, self._on_keyup)
		self.parent = self
		self.gui = self

	def draw(self, event_list, frame_time):
		self.frame_time = frame_time
		self.eventmgr.run(event_list)
		for child in self.child_elements:
			child.handle_events(event_list)
		for child in self.child_elements:
			child.draw(event_list)

	def add(self, elem):
		container.add(self, elem)
		self.focus_grid = elem.get_focus_grid()
		elem.set_gui(self)
		elem.set_target_surface(self.surface)
		for y in range(self.focus_grid.h):
			for x in range(self.focus_grid.w):
				if self.focus_grid[x][y]:
					self.focus_grid[x][y].focus_coords = (x,y)
		self.focus_grid.item(self.focus_coords).focus()
		added = []
		for y in range(self.focus_grid.h):
			for x in range(self.focus_grid.w):
				item = self.focus_grid.item((x, y))
				if item.id not in added:
					item.tab_order = len(self.tabs)
					self.tabs.append((x, y))
					added.append(item.id)

	def get_element(self, elem_id):
		global elements
		return elements[elem_id]

	def set_focus(self, focus_coords):
		old_focus = self.focus_grid.item(self.focus_coords)
		new_focus = self.focus_grid.item(focus_coords)
		if self.focus_coords != None and old_focus != new_focus:
			self.focus_grid.item(self.focus_coords).blur()
		new_focus.focus_coords = focus_coords
		self.focus_coords = focus_coords

	def tab(self, focus_coords, options={}):
		#self.focus_coords = focus_coords
		self.focus_grid.item(focus_coords).focus()
		self.set_focus(focus_coords)

	def tab_right(self):
		next_tab_id = self.focus_grid.item(self.focus_coords).tab_order+1
		if next_tab_id == len(self.tabs):
			next_tab_id = 0
		self.tab(self.tabs[next_tab_id])

	def tab_left(self):
		next_tab_id = self.focus_grid.item(self.focus_coords).tab_order-1
		if next_tab_id < 0:
			next_tab_id = len(self.tabs)-1
		self.tab(self.tabs[next_tab_id])

	def item_right(self):
		current_id = self.focus_grid.item(self.focus_coords).id
		focus_coords = self.focus_coords
		for i in range(self.focus_grid.w):
			focus_coords = self.focus_grid.next_coords_from(focus_coords, "right")
			if self.focus_grid.item(focus_coords).id != current_id:
				self.tab(focus_coords)
				break

	def item_left(self):
		current_id = self.focus_grid.item(self.focus_coords).id
		focus_coords = self.focus_coords
		for i in range(self.focus_grid.w):
			focus_coords = self.focus_grid.next_coords_from(focus_coords, "left")
			if self.focus_grid.item(focus_coords).id != current_id:
				self.tab(focus_coords)
				break

	def item_up(self):
		current_id = self.focus_grid.item(self.focus_coords).id
		focus_coords = self.focus_coords
		for i in range(self.focus_grid.w):
			focus_coords = self.focus_grid.next_coords_from(focus_coords, "up")
			if self.focus_grid.item(focus_coords).id != current_id:
				self.tab(focus_coords)
				break

	def item_down(self):
		current_id = self.focus_grid.item(self.focus_coords).id
		focus_coords = self.focus_coords
		for i in range(self.focus_grid.w):
			focus_coords = self.focus_grid.next_coords_from(focus_coords, "down")
			if self.focus_grid.item(focus_coords).id != current_id:
				self.tab(focus_coords)
				break

	def next_element(self):
		return None

	def prev_element(self):
		return None

	def element_above(self):
		return None

	def press_focused(self):
		focused = self.focus_grid.item(self.focus_coords)
		focused.press()

	def unpress_focused(self):
		focused = self.focus_grid.item(self.focus_coords)
		focused.unpress(1)

	def mouse_over(self, event=None):
		pass

	def _on_mouse_motion(self, event):
		self.mouse_pos = event.pos
		hoverable._on_mousemotion(self, event)

	def _on_keydown(self, event):
		if event.key in [K_LSHIFT, K_RSHIFT]:
			self.shift = True
		if event.key in [K_LCTRL, K_RCTRL]:
			self.ctrl = True
		if event.key in [K_LALT, K_RALT]:
			self.alt = True
		if event.key in [K_KP_ENTER, K_RETURN]:
			self.press_focused()
		if event.key == self.keymap.tab:
			if self.shift:
				self.tab_left()
			else:
				self.tab_right()
		elif event.key == self.keymap.right:
			self.item_right()
		elif event.key == self.keymap.left:
			self.item_left()
		elif event.key == self.keymap.up:
			self.item_up()
		elif event.key == self.keymap.down:
			self.item_down()

	def _on_keyup(self, event):
		if event.key in [K_LSHIFT, K_RSHIFT]:
			self.shift = False
		if event.key in [K_LCTRL, K_RCTRL]:
			self.ctrl = False
		if event.key in [K_LALT, K_RALT]:
			self.alt = False
		if event.key in [K_KP_ENTER, K_RETURN]:
			self.unpress_focused()
