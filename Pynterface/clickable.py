import pygame
from events import *
from pygame.locals import *

class clickable:
	rect = None
	click_enabled = True
	mouse_button_down = False
	last_pos = None
	pressed = False
	double_click_timeout = 100
	double_click_timer = 0
	frame_time = 0

	def __init__(self):
		self.options["pressed"] = {}
		self.event_type_bindings.append("CLICK")
		self.event_type_bindings.append("DOUBLECLICK")

	def set_gui(self, gui):
		self.eventmgr.bind(MOUSEBUTTONDOWN, self._on_mousebutton_down)
		self.eventmgr.bind(MOUSEBUTTONUP, self._on_mousebutton_up)

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

	def unpress(self, click=0):
		self.pressed = False
		self.double_click_timer = 0
		if click:
			if click == 1:
				pygame.event.post(pygame.event.Event(PYNTERFACE_EVENT, {"pface_type": "CLICK", "elem": self, "pos":self.gui.mouse_pos}))
			elif click == 2:
				pygame.event.post(pygame.event.Event(PYNTERFACE_EVENT, {"pface_type": "DOUBLECLICK", "elem": self, "pos":self.gui.mouse_pos}))

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
