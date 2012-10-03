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
				if self.onMouseDown and self.rect.collidepoint(event.pos):
					self.pressed = True
					self.onMouseDown(self, event)
			elif event.type == MOUSEBUTTONUP:
				if self.pressed:
					if self.onMouseUp:
						self.onMouseUp(self, event)
					if self.onClick and self.rect.collidepoint(event.pos):
						self.onClick(self, event)
					self.pressed = False

	def press(self):
		self.pressed = True
		if self.onMouseDown:
			self.onMouseDown(self, None)

	def unpress(self):
		self.pressed = False
		if self.onMouseUp:
			self.onMouseUp(self, None)
		if self.onClick:
			self.onClick(self, None)