import pygame
from pygame.locals import *

class hoverable:
	rect = None
	hover = False
	last_hover = False
	enabled = True

	onMouseOver = None
	onMouseOut = None

	def __init__(self):
		self.options["hover"] = {}

	def draw(self, events):
		if not self.enabled:
			return
		for event in events:
			if event.type == MOUSEMOTION:
				if self.rect.collidepoint(event.pos):
					self.hover = True
				else:
					self.hover = False
				self.mouse_over(event)
				self.mouse_out(event)
				self.last_hover = self.hover


	def mouse_over(self, event):
		if self.hover and not self.last_hover and self.onMouseOver:
			self.onMouseOver(self, event)

	def mouse_out(self, event):
		if not self.hover and self.last_hover and self.onMouseOut:
			self.onMouseOut(self, event)