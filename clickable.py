import pygame
from pygame.locals import *

class clickable:
	rect = None
	enabled = True
	state = ""
	onClick = None
	onMouseDown = None
	onMouseUp = None

	def draw(self, events):
		if not self.enabled:
			return
		for event in events:
			if event.type == MOUSEBUTTONDOWN:
				if self.onMouseDown and self.rect.collidepoint(event.pos):
					self.state = "down"
					self.onMouseDown(self, event)
			elif event.type == MOUSEBUTTONUP:
				if self.state == "down":
					if self.onMouseUp:
						self.onMouseUp(self, event)
					if self.onClick and self.rect.collidepoint(event.pos):
						self.onClick(self, event)
					self.state = "up"