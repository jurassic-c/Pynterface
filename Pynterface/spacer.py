from element import *
import pygame
from pygame.locals import *

class spacer(element):
	def __init__(self, height, width):
		element.__init__(self)
		self.rect = pygame.Rect((0,0,width,height))

	def set_target_surface(self, surface):
		element.set_target_surface(self, surface)

	def draw(self, events):
		element.draw(self, events)
		#pygame.draw.rect(self.target_surface, (0,0,255), self.rect, 2)
