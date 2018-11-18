import pygame
from events import *
from pygame.locals import *

class clickable:
	rect = None
	click_enabled = True
	mouse_button_down = False
	last_pos = None
	pressed = False
	double_click_timeout = 200
	double_click_timer = 0
	frame_time = 0

	def __init__(self):
		self.options["pressed"] = {}

	def set_gui(self, gui):
		gui.eventmgr.bind(MOUSEBUTTONDOWN, self._on_mousebutton_down)
		gui.eventmgr.bind(MOUSEBUTTONUP, self._on_mousebutton_up)

	def set_target_surface(self, surface):
		pass

	def draw(self, events):
		if self.pressed and not self.mouse_button_down:
			self.double_click_timer+= self.gui.frame_time
			if self.double_click_timer > self.double_click_timeout:
				self.unpress(1)

	def double_click(self):
		self.pressed = False
		self.double_click_timer = 0
		self.unpress(2)


	def press(self):
		self.pressed = True
		self.double_click_timer = 0
		self.focus()
		self.gui.set_focus(self.focus_coords)
		self.eventmgr.run([pygame.event.Event(MOUSEBUTTONDOWN, {"elem": self, "pos":self.gui.mouse_pos})])

	def unpress(self, click=0):
		self.pressed = False
		self.double_click_timer = 0
		self.eventmgr.run([pygame.event.Event(MOUSEBUTTONUP, {"elem": self, "pos":self.gui.mouse_pos})])
		if click:
			if click == 1:
				self.eventmgr.run([pygame.event.Event(CLICK, {"elem": self, "pos":self.gui.mouse_pos})])
			elif click == 2:
				self.eventmgr.run([pygame.event.Event(DOUBLECLICK, {"elem": self, "pos":self.gui.mouse_pos})])

	def _on_mousebutton_down(self, event):
		if not self.click_enabled:
			return
		if event.button != 1:
			return
		self.last_pos = event.pos
		self.mouse_button_down = True
		if self.rect.collidepoint(self.last_pos):
			if self.pressed:
				self.double_click()
			else:
				self.press()

	def _on_mousebutton_up(self, event):
		if not self.click_enabled:
			return
		self.last_pos = event.pos
		self.mouse_button_down = False
		if self.pressed:
			if not self.rect.collidepoint(self.last_pos):
				self.unpress()
