import pygame
from pygame.locals import *

class hoverable:
	rect = None
	pos_mouse_over = False
	last_pos_mouse_over = False
	enabled = True

	onMouseOver = None
	onMouseOut = None

	def draw(self, events):
		if not self.enabled:
			return
		for event in events:
			if event.type == MOUSEMOTION:
				if self.rect.collidepoint(event.pos):
					self.pos_mouse_over = True
				else:
					self.pos_mouse_over = False
				self.mouse_over(event)
				self.mouse_out(event)
				self.last_pos_mouse_over = self.pos_mouse_over


	def mouse_over(self, event):
		if self.pos_mouse_over and not self.last_pos_mouse_over and self.onMouseOver:
			self.onMouseOver(self, event)

	def mouse_out(self, event):
		if not self.pos_mouse_over and self.last_pos_mouse_over and self.onMouseOut:
			self.onMouseOut(self, event)