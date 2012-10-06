import pygame
from pygame.locals import *

class clickable:
	rect = None
	enabled = True
	onClick = None
	onMouseDown = None
	onMouseUp = None
	pressed = False

	def __init__(self):
		self.options["pressed"] = {}

	def draw(self, events):
		if not self.enabled:
			return
		for event in events:
			if event.type == MOUSEBUTTONDOWN:
				if self.rect.collidepoint(event.pos):
					self.press()
			elif event.type == MOUSEBUTTONUP:
				if self.pressed:
					click = False
					if self.rect.collidepoint(event.pos):
						click = True
					self.unpress(click)

	def press(self):
		self.pressed = True
		if self.onMouseDown:
			self.focus()
			self.gui.set_focus(self.focus_coords)
			self.onMouseDown(self, None)

	def unpress(self, do_click=False):
		self.pressed = False
		if self.onMouseUp:
			self.onMouseUp(self, None)
		if do_click and self.onClick:
			self.onClick(self, None)