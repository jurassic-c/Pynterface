from Pynterface import *
import pygame
from pygame.locals import *

class image(element):
	rect = None
	image_surface = None
	def __init__(self, image_path):
		self.image_surface = pygame.image.load(image_path)
		self.rect = pygame.Rect(self.image_surface.get_rect().x, self.image_surface.get_rect().y, self.image_surface.get_rect().width, self.image_surface.get_rect().height)
		element.__init__(self)

	def draw(self, events):
		self.target_surface.blit(self.image_surface, self.rect)
		element.draw(self, events)
