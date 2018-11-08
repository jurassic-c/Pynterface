import pygame
import pygame.image
import pygame.rect
import pygame.surface

class Nineslice:
	radius = None
	top_left = None
	top = None
	top_right = None
	left = None
	center = None
	right = None
	bottom_left = None
	bottom = None
	bottom_right = None
	def __init__(self, image_surf, radius):
		self.radius = radius
		image_rect = image_surf.get_rect()
		if image_rect.width-(radius * 2) < 1:
			raise ValueError("radius must be less than half of the width or height, whichever is lower")
		if image_rect.height-(radius * 2) < 1:
			raise ValueError("radius must be less than half of the width or height, whichever is lower")
		# setup objects
		self.top_left = {"rect": pygame.Rect(0,0,radius,radius)}
		self.top = {"rect": pygame.Rect(0,0,image_rect.width-(radius*2), radius)}
		self.top_right = {"rect": pygame.Rect(0,0,radius,radius)}
		self.left = {"rect": pygame.Rect(0,0,radius, image_rect.height-(radius*2))}
		self.center = {"rect": pygame.Rect(0,0,image_rect.width-(radius*2), image_rect.height-(radius*2))}
		self.right = {"rect": pygame.Rect(0,0,radius, image_rect.height-(radius*2))}
		self.bottom_left = {"rect": pygame.Rect(0,0,radius,radius)}
		self.bottom = {"rect": pygame.Rect(0,0,image_rect.width-(radius*2), radius)}
		self.bottom_right = {"rect": pygame.Rect(0,0,radius,radius)}

		# Blit surfaces
		self.top_left["surf"] = pygame.Surface((radius, radius))
		self.top_left["surf"].blit(image_surf, (0,0))
		
		self.top["surf"] = pygame.Surface((image_rect.width-(radius*2), radius))
		self.top["surf"].blit(image_surf, (0-radius,0))

		self.top_right["surf"] = pygame.Surface((radius, radius))
		self.top_right["surf"].blit(image_surf, (0-image_rect.w+radius,0))

		self.left["surf"] = pygame.Surface((radius, image_rect.height-(radius*2)))
		self.left["surf"].blit(image_surf, (0,0-radius))

		self.center["surf"] = pygame.Surface((image_rect.width-(radius*2), image_rect.height-(radius*2)))
		self.center["surf"].blit(image_surf, (0-radius,0-radius))

		self.right["surf"] = pygame.Surface((radius, image_rect.height-(radius*2)))
		self.right["surf"].blit(image_surf, (0-image_rect.width+radius,0-radius))

		self.bottom_left["surf"] = pygame.Surface((radius, radius))
		self.bottom_left["surf"].blit(image_surf, (0,0-image_rect.height+radius))
		
		self.bottom["surf"] = pygame.Surface((image_rect.width-(radius*2), radius))
		self.bottom["surf"].blit(image_surf, (0-radius,0-image_rect.height+radius))

		self.bottom_right["surf"] = pygame.Surface((radius, radius))
		self.bottom_right["surf"].blit(image_surf, (0-image_rect.w+radius,0-image_rect.height+radius))

	def apply_to_surface(self, surf):
		image_rect = surf.get_rect()
		#### corners
		surf.blit(self.top_left["surf"], (0,0))
		surf.blit(self.top_right["surf"], (image_rect.width-self.radius, 0))
		surf.blit(self.bottom_left["surf"], (0, image_rect.height-self.radius))
		surf.blit(self.bottom_right["surf"], (image_rect.width-self.radius, image_rect.height-self.radius))

		#### edges
		# top
		for i in range((image_rect.width-self.radius) / self.top["rect"].width):
			surf.blit(self.top["surf"], (self.radius+(i*self.top["rect"].width), 0))
		# left
		for i in range((image_rect.height-self.radius) / self.left["rect"].height):
			surf.blit(self.left["surf"], (0,self.radius+(i*self.left["rect"].height)))
		# right
		for i in range((image_rect.height-self.radius) / self.right["rect"].height):
			surf.blit(self.right["surf"], (image_rect.width-self.radius,self.radius+(i*self.left["rect"].height)))
		# bottom
		for i in range((image_rect.width-self.radius) / self.bottom["rect"].width):
			surf.blit(self.bottom["surf"], (self.radius+(i*self.top["rect"].width), 0+image_rect.height-self.radius))

		#### center
		
		for x in range((image_rect.width-self.radius) / self.center["rect"].width):
			for y in range((image_rect.height-self.radius) / self.center["rect"].height):
				surf.blit(self.center["surf"], (self.radius+(x*self.center["rect"].width), self.radius+(y*self.center["rect"].height)))

