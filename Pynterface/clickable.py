import pygame
from pygame.locals import *

class clickable:
	rect = None
	enabled = True
	onClick = None
	onDoubleClick = None
	onMouseDown = None
	onMouseUp = None
	mouse_button_down = False
	last_pos = None
	pressed = False
	double_click_timeout = 200
	double_click_timer = 0
	frame_time = 0

	def __init__(self):
		self.options["pressed"] = {}

	def draw(self, events):
		if not self.enabled:
			return
		for event in events:
			if event.type == MOUSEBUTTONDOWN:
				self.last_pos = event.pos
				self.mouse_button_down = True
				if self.rect.collidepoint(self.last_pos):
					if self.pressed:
						self.double_click()
					else:
						self.press()
			elif event.type == MOUSEBUTTONUP:
				self.last_pos = event.pos
				self.mouse_button_down = False
				if self.pressed:
					if not self.rect.collidepoint(self.last_pos):
						self.unpress()

		if self.pressed and not self.mouse_button_down:
			self.double_click_timer+= self.gui.frame_time
			if self.double_click_timer > self.double_click_timeout:
				if self.rect.collidepoint(self.gui.mouse_pos):
					self.unpress(1)

	def double_click(self):
		self.pressed = False
		self.double_click_timer = 0
		self.unpress(2)


	def press(self):
		self.pressed = True
		if self.onMouseDown:
			self.double_click_timer = 0
			self.focus()
			self.gui.set_focus(self.focus_coords)
			self.onMouseDown(self, None)

	def unpress(self, click=0):
		self.pressed = False
		self.double_click_timer = 0
		if self.onMouseUp:
			self.onMouseUp(self, None)
		if click:
			if click == 1 and self.onClick:
				self.onClick(self, None)
			elif click == 2 and self.onDoubleClick:
				self.onDoubleClick(self, None)