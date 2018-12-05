import pygame
from events import *
from pygame.locals import *
import pygame.freetype

class textable:
	text = ""
	font = None
	text_surf = None
	text_rect = None
	font_size = 10
	max_width = -1
	max_width_text_align = "left"
	horizontal_padding = 0
	def __init__(self):
		pass

	def set_gui(self, gui):
		self.gui = gui

	def set_target_surface(self, surface):
			pass

	def draw(self, events):
		if not self.font:
			font_path = "assets/fonts/open-sans/OpenSans-Regular.ttf"
			self.font_size = 10
			text_color = None
			if self.options.has_key("font_path"):
				font_path = self.options["font_path"]
			if self.options.has_key("font_size"):
				self.font_size = self.options["font_size"]
			if self.options.has_key("text_color"):
				text_color = self.options["text_color"]
			self.font = pygame.freetype.Font(font_path, size=self.font_size)
			if text_color:
				self.font.fgcolor = text_color

			
		if self.options.has_key("horizontal_padding"):
			self.horizontal_padding = self.options["horizontal_padding"]
		if self.options.has_key("max_width"):
			self.max_width = self.options["max_width"]
		if self.options.has_key("max_width_text_align"):
			self.max_width_text_align = self.options["max_width_text_align"]
		opt_text = ""
		if self.options.has_key("text"):
			opt_text = self.options["text"]
		if opt_text != self.text:
			miny = self._get_text_miny(self.font.get_metrics(opt_text))
			text_height = self.font.get_sized_height(self.font_size)
			self.font.origin = True
			text_surf, text_rect = self.font.render(opt_text)
			text_width = text_rect.width+2*self.horizontal_padding
			if text_width < 0:
				text_width = 0
			if self.max_width >= 0 and text_width > self.max_width:
				text_width = self.max_width
			crop_width = text_width - 2*self.horizontal_padding
			crop_offset = 0
			if self.max_width_text_align == "right" and text_rect.w - text_width + 2*self.horizontal_padding> 0:
				crop_offset = text_rect.w - text_width + 2*self.horizontal_padding
			self.text_surf = pygame.Surface((text_width, text_height), SRCALPHA)
			self.text_surf.blit(text_surf, (self.horizontal_padding,self.font_size-text_rect.h-miny), (crop_offset,0,crop_width,text_rect.h))
			self.text_rect = self.text_surf.get_rect()
		self.text = opt_text

		# Blit Text
		if self.text:
			rectSurf = pygame.Surface((self.rect.w, self.rect.h), SRCALPHA)
			text_position = "center"
			if self.options.has_key("text_position"):
					text_position = self.options["text_position"]
			rectSurf.blit(self.text_surf, self.get_text_position_rect(self.text_surf, self.rect, text_position));
			self.target_surface.blit(rectSurf, self.rect)

	def get_text_position_rect(self, image_surf, target_rect, position="center"):
			top = 0
			left = 0
			image_rect = image_surf.get_rect()
			if position == "top_left":
					left = 0
					top = 0
			elif position == "top":
					left = (target_rect.width - image_rect.w) / 2
					top = 0
			elif position == "top_right":
					left = target_rect.width - image_rect.w
					top = 0
			elif position == "left":
					left = 0
					top = (target_rect.height - image_rect.h) / 2
			elif position == "center":
					left = (target_rect.width - image_rect.w) / 2
					top = (target_rect.height - image_rect.h) / 2
			elif position == "right":
					left = (target_rect.width - image_rect.w)
					top = (target_rect.height - image_rect.h) / 2
			elif position == "bottom_left":
					left = 0
					top = target_rect.height - image_rect.h
			elif position == "bottom":
					left = (target_rect.width - image_rect.w) / 2
					top = target_rect.height - image_rect.h
			elif position == "bottom_right":
					left = target_rect.width - image_rect.w
					top = target_rect.height - image_rect.h
			return (left, top)
		
	def _get_text_minx(self, metrics):
		minx = 0
		for m in metrics:
			if m[0] < m:
				minx = m[0]
		return minx

	def _get_text_miny(self, metrics):
		miny = 0
		for m in metrics:
			if not m:
				continue
			# Returning biggest absolute because the miny metric tends to be
			# a crazy huge number like 4294967292
			if abs(m[2]) > miny:
				miny = m[2]
		return miny
