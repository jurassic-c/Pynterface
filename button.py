from Pynterface import *
import pygame
from pygame.locals import *

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
		textable.set_gui(self, gui)

	def set_target_surface(self, surface):
		element.set_target_surface(self, surface)
		clickable.set_target_surface(self, surface)
		hoverable.set_target_surface(self, surface)
		textable.set_target_surface(self, surface)
	
	def remove_hover(self, event=None):
		self.hover = False
		self.mouse_out(event)
		self.last_hover = False

	def draw(self, events):
		opt_val = ""
		if self.options.has_key("hover") and self.options["hover"].has_key("image"):
			opt_val = self.options["hover"]["image"]
		self.setup_state_image(opt_val, "hover")
		opt_val = ""
		if self.options.has_key("focused") and self.options["focused"].has_key("image"):
			opt_val = self.options["focused"]["image"]
		self.setup_state_image(opt_val, "focused")
		opt_val = ""
		if self.options.has_key("pressed") and self.options["pressed"].has_key("image"):
			opt_val = self.options["pressed"]["image"]
		self.setup_state_image(opt_val, "pressed")
		element.draw(self, events)
		clickable.draw(self, events)
		hoverable.draw(self, events)

		rectSurf = pygame.Surface((self.rect.w, self.rect.h))
		width = 0
		if not self.filled:
			width = 1

		color = (122, 0, 0)
		image_position = "center"
		image_key = None
		if self.options.has_key("image_position"):
			image_position = self.options["image_position"]
		if self.options.has_key("color"):
			color = self.options["color"]
		if self.image_surfaces.has_key("default"):
			image_key = "default"
		if self.focused:
			if self.options["focused"].has_key("color"):
				color = self.options["focused"]["color"]
			if self.image_surfaces.has_key("focused"):
				image_key = "focused"
		if self.hover:
			if self.options["hover"].has_key("color"):
				color = self.options["hover"]["color"]
			if self.image_surfaces.has_key("hover"):
				image_key = "hover"
		if self.pressed:
			if self.options["pressed"].has_key("color"):
				color = self.options["pressed"]["color"]
			if self.image_surfaces.has_key("pressed"):
				image_key = "pressed"
		if image_key:
			rectSurf.blit(self.image_surfaces[image_key],self.get_image_position_rect(self.image_surfaces["default"], self.rect, image_position))
		elif not self.options.has_key("image"):
			pygame.draw.rect(rectSurf, color, pygame.Rect(0, 0, self.rect.width, self.rect.height), width)

		self.target_surface.blit(rectSurf, self.rect)
		textable.draw(self, events)

	def get_image_position_rect(self, image_surf, target_rect, position="center"):
		top = 0
		left = 0
		image_rect = image_surf.get_rect()
		if position == "top_left":
			left = 0
			top = 0
		elif position == "top":
			left = abs(target_rect.width - image_rect.w) / 2
			top = 0
		elif position == "top_right":
			left = abs(target_rect.width - image_rect.w)
			top = 0
		elif position == "left":
			left = 0
			top = abs(target_rect.height - image_rect.h) / 2
		elif position == "center":
			left = abs(target_rect.width - image_rect.w) / 2
			top = abs(target_rect.height - image_rect.h) / 2
		elif position == "right":
			left = abs(target_rect.width - image_rect.w)
			top = abs(target_rect.height - image_rect.h) / 2
		elif position == "bottom_left":
			left = 0
			top = abs(target_rect.height - image_rect.h)
		elif position == "bottom":
			left = abs(target_rect.width - image_rect.w) / 2
			top = abs(target_rect.height - image_rect.h)
		elif position == "bottom_right":
			left = abs(target_rect.width - image_rect.w)
			top = abs(target_rect.height - image_rect.h)
		return (left, top)
