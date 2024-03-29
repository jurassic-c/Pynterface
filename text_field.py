from Pynterface import *
import pygame
from pygame.locals import *
from Pynterface.events import *

class text_field(element, clickable, textable):
	focused_image_path = ""
	value = ""
	last_value = ""

	def __init__(self, width, height, x=0, y=0):
		self.rect = pygame.Rect(x, y, width, height)
		element.__init__(self)
		clickable.__init__(self)
		self.event_type_bindings.append("CHANGE")
		self.eventmgr.bind(KEYDOWN, self._on_keydown)
		self.max_width_text_align = "right"
		self.options["text"] = ""

	def _on_keydown(self, event):
		if not self.focused:
			return
		if event.key in [8]:
			if len(self.value):
				self.value = self.value[:-1]
		else:
			self.value+= event.unicode

	def set_gui(self, gui):
		element.set_gui(self, gui)
		clickable.set_gui(self, gui)
		textable.set_gui(self, gui)

	def set_target_surface(self, surface):
		element.set_target_surface(self, surface)
		clickable.set_target_surface(self, surface)
		textable.set_target_surface(self, surface)

	def handle_events(self, events):
		element.handle_events(self, events)

	def draw(self, events):
		if self.last_value != self.value:
			change_event = pygame.event.Event(PYNTERFACE_EVENT, {"pface_type": "CHANGE", "elem": self, "old_value": self.last_value, "new_value": self.value})
			pygame.event.post(change_event)
		self.last_value = self.value
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

		rectSurf = pygame.Surface((self.rect.w, self.rect.h))
		width = 0

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

		if self.focused:
			self.options["text"]+= "_"

		textable.draw(self, events)

		self.options["text"] = self.value

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
