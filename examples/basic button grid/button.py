from Pynterface import *
import pygame
from pygame.locals import *

class button(element, clickable, hoverable):
	filled = True

	def __init__(self, width, height, x=0, y=0):
		self.rect = pygame.Rect(x, y, width, height)
		element.__init__(self)
		clickable.__init__(self)
		hoverable.__init__(self)

	def draw(self, events):
		rectSurf = pygame.Surface((self.rect.w, self.rect.h))
		width = 0
		if not self.filled:
			width = 1

		color = (122, 0, 0)
		if self.options.has_key("color"):
			color = self.options["color"]
		if self.focused:
			if self.options["focused"].has_key("color"):
				color = self.options["focused"]["color"]
		if self.hover and self.options["hover"].has_key("color"):
			color = self.options["hover"]["color"]
		if self.pressed:
			if self.options["pressed"].has_key("color"):
				color = self.options["pressed"]["color"]
		pygame.draw.rect(rectSurf, color, pygame.Rect(0, 0, self.rect.width, self.rect.height), width)
		self.gui.surface.blit(rectSurf, self.rect)

		element.draw(self, events)
		clickable.draw(self, events)
		hoverable.draw(self, events)