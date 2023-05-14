from element import *
from textable import *
import pygame
from pygame.locals import *

class label(element, textable):
	def __init__(self, height, width, text):
		element.__init__(self)
		textable.__init__(self)
		self.rect = pygame.Rect((0,0,width,height))
		self.options["text"] = text

	def set_target_surface(self, surface):
		element.set_target_surface(self, surface)

	def draw(self, events):
		textable.draw(self, events)
