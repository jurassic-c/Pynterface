from Pynterface import *
import pygame
from pygame.locals import *
import pygame.freetype

class button(element, clickable, hoverable, textable):
	filled = True
	hover_image_path = ""
	pressed_image_path = ""
	focused_image_path = ""

	def __init__(self, width, height, x=0, y=0):
		self.rect = pygame.Rect(x, y, width, height)
		element.__init__(self)
		clickable.__init__(self)
		hoverable.__init__(self)

	def set_gui(self, gui):
		element.set_gui(self, gui)
		clickable.set_gui(self, gui)
		hoverable.set_gui(self, gui)

	def draw(self, events):
		self.setup_hover_image()
		self.setup_pressed_image()
		self.setup_focused_image()
		rectSurf = pygame.Surface((self.rect.w, self.rect.h))
		width = 0
		if not self.filled:
			width = 1

		color = (122, 0, 0)
		is_default = True
		if self.options.has_key("color"):
			color = self.options["color"]
		if self.focused:
			is_default = False
			if self.options["focused"].has_key("color"):
				color = self.options["focused"]["color"]
			if self.image_surfaces.has_key("focused"):
				rectSurf.blit(self.image_surfaces["focused"], self.image_surfaces["focused"].get_rect())
		if self.hover:
			is_default = False
			if self.options["hover"].has_key("color"):
				color = self.options["hover"]["color"]
			if self.image_surfaces.has_key("hover"):
				rectSurf.blit(self.image_surfaces["hover"], self.image_surfaces["hover"].get_rect())
		if self.pressed:
			is_default = False
			if self.options["pressed"].has_key("color"):
				color = self.options["pressed"]["color"]
			if self.image_surfaces.has_key("pressed"):
				rectSurf.blit(self.image_surfaces["pressed"], self.image_surfaces["pressed"].get_rect())
		if self.image_surfaces.has_key("default") and is_default:
			pygame.draw.rect(rectSurf, color, pygame.Rect(0, 0, self.rect.width, self.rect.height), width)
			rectSurf.blit(self.image_surfaces["default"], self.image_surfaces["default"].get_rect())


		# Blit Text
		if self.text:
			text_position = "center"
			if self.options.has_key("text_position"):
				text_position = self.options["text_position"]
			rectSurf.blit(self.text_surf, self.get_text_position_rect(self.text_surf, self.rect, text_position));
		self.gui.surface.blit(rectSurf, self.rect)

		element.draw(self, events)
		clickable.draw(self, events)
		hoverable.draw(self, events)
		textable.draw(self, events)

	def setup_hover_image(self):
		opt_val = ""
		if self.options.has_key("hover") and self.options["hover"].has_key("image"):
			opt_val = self.options["hover"]["image"]
		if opt_val == self.hover_image_path:
			return
		self.hover_image_path = opt_val
		if not self.hover_image_path:
			del self.image_surfaces["hover"]
			return

		if self.options.has_key("nineslice_radius"):
			radius = self.options["nineslice_radius"]

		image_surf = pygame.image.load(self.options["hover"]["image"])
		image_rect = image_surf.get_rect()
		nineslice = Nineslice(image_surf, self.options["nineslice_radius"])
		self.image_surfaces["hover"] = pygame.Surface((self.rect.width, self.rect.height))
		nineslice.apply_to_surface(self.image_surfaces["hover"])

	def setup_pressed_image(self):
		opt_val = ""
		if self.options.has_key("pressed") and self.options["pressed"].has_key("image"):
			opt_val = self.options["pressed"]["image"]
		if opt_val == self.pressed_image_path:
			return
		self.pressed_image_path = opt_val
		if not self.pressed_image_path:
			del self.image_surfaces["pressed"]
			return

		if self.options.has_key("nineslice_radius"):
			radius = self.options["nineslice_radius"]

		image_surf = pygame.image.load(self.options["pressed"]["image"])
		image_rect = image_surf.get_rect()
		nineslice = Nineslice(image_surf, self.options["nineslice_radius"])
		self.image_surfaces["pressed"] = pygame.Surface((self.rect.width, self.rect.height))
		nineslice.apply_to_surface(self.image_surfaces["pressed"])

	def setup_focused_image(self):
		opt_val = ""
		if self.options.has_key("focused") and self.options["focused"].has_key("image"):
			opt_val = self.options["focused"]["image"]
		if opt_val == self.focused_image_path:
			return
		self.focused_image_path = opt_val
		if not self.focused_image_path:
			del self.image_surfaces["focused"]
			return

		if self.options.has_key("nineslice_radius"):
			radius = self.options["nineslice_radius"]

		image_surf = pygame.image.load(self.options["focused"]["image"])
		image_rect = image_surf.get_rect()
		nineslice = Nineslice(image_surf, self.options["nineslice_radius"])
		self.image_surfaces["focused"] = pygame.Surface((self.rect.width, self.rect.height))
		nineslice.apply_to_surface(self.image_surfaces["focused"])
