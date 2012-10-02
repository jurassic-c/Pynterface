import pygame
from container import *

class vbox(container):
	padding = 0

	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)
		container.__init__(self)

	def add(self, elem):
		elem.move(self.rect.x, self.rect.y + self.rect.h + self.padding*len(self.child_elements))
		if elem.rect.w > self.rect.w:
			self.resize(elem.rect.w, self.rect.h)
		self.resize(elem.rect.w, self.rect.h + elem.rect.h)
		container.add(self, elem)