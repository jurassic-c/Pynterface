###
# Options:
#
# scrollbar_width:				Integer. Width in pixels of the scrollbars. Default 15
# bg_color:						Pygame Color. Background color to use.
# fg_color:						Pygame Color. Foreground or handle color to use.
# fg_image:						String.	Path to Foreground or handle image to use.
# fg_image_nineslice_radius:	Integer. Nineslice radius to use for foreground image
#

import pygame
from events import *
from pygame.locals import *
from container import *
from nineslice import Nineslice

class scrollable(container):
	width = 0
	height = 0
	surf = None
	rect = None
	show_vert_multiplier = 0
	show_horiz_multiplier = 0
	y_offset = 0
	handle_y_offset = 0
	x_offset = 0
	handle_x_offset = 0
	max_y_offset = 0
	max_x_offset = 0
	fg_color = None
	bg_color = None
	fg_image_path = ""
	fg_image = ""
	fg_image_nineslice = ""
	bg_image_path = ""
	bg_image = ""
	bg_image_nineslice = ""
	scrollbar_width = 15
	last_pos = None
	handles_dirty = False
	vert_handle_surf = None
	horiz_handle_surf = None
	mouse_down = False
	drag_origin = (0,0)
	dragging_horiz = False
	dragging_vert = False
	scroll_x = 0
	scroll_y = 0
	scroll_vert_pos = 0
	scroll_horiz_pos = 0
	def __init__(self, w, h):
		container.__init__(self)
		self.width = w
		self.height = h
		self.surf = pygame.Surface((w, h))
		self.rect = self.surf.get_rect()

	def _on_mousemotion(self, event):
		if not self.mouse_down:
			return
		if not self.hover_enabled:
			self.hover = False
			return
		if event.type == MOUSEMOTION:
			if self.dragging_vert:
				y_diff = event.pos[1] - self.drag_origin[1]
				self.scroll_by_bar_vert(y_diff)
			if self.dragging_horiz:
				x_diff = event.pos[0] - self.drag_origin[0]
				self.scroll_by_bar_horiz(x_diff)

	def _on_mouse_event(self, event):
		self.last_pos = event.pos
		y_off = self.y_offset
		x_off = self.x_offset
		if not self.rect.collidepoint(self.last_pos):
			return
		scroll_multiplier=2
		if event.button == 1:
			self.mouse_down = True
			vert_rect = self.vert_handle_surf.get_rect()
			horiz_rect = self.horiz_handle_surf.get_rect()
			if horiz_rect.collidepoint((event.pos[0]-self.handle_x_offset, event.pos[1]-self.rect.h+self.scrollbar_width)):
				self.dragging_horiz = True
				self.drag_origin = event.pos
			if vert_rect.collidepoint((event.pos[0]-self.rect.w+self.scrollbar_width, event.pos[1]-self.handle_y_offset)):
				self.dragging_vert = True
				self.drag_origin = event.pos
		if event.button == 4:
			y_off-=scroll_multiplier
		if event.button == 5:
			y_off+=scroll_multiplier
		if event.button == 6:
			x_off-=scroll_multiplier
		if event.button == 7:
			x_off+=scroll_multiplier

		self.scroll(x_off, y_off, True)

	def scroll_by_bar_vert(self, y_off):
		handle_h = self.rect.h**2 / self.child_elements[0].rect.h
		remainder_y = self.rect.h - handle_h
		scroll_percent_y = float(float(y_off) / remainder_y)
		scroll_y = scroll_percent_y * (self.child_elements[0].rect.h - self.rect.h)

		self.scroll_y = scroll_y

		self.scroll(self.x_offset, scroll_y+self.scroll_vert_pos)

	def scroll_by_bar_horiz(self, x_off):
		handle_w = self.rect.w**2 / self.child_elements[0].rect.w
		remainder_x = self.rect.w - handle_w
		scroll_percent_x = float(float(x_off) / remainder_x)
		scroll_x = scroll_percent_x * (self.child_elements[0].rect.w - self.rect.w)

		self.scroll_x = scroll_x

		self.scroll(scroll_x+self.scroll_horiz_pos, self.y_offset)


	def scroll(self, x_off, y_off, save_pos = False):

		if y_off<0:
			y_off=0
		if y_off>self.max_y_offset:
			y_off = self.max_y_offset

		if x_off<0:
			x_off=0
		if x_off>self.max_x_offset:
			x_off = self.max_x_offset

		self.y_offset = y_off
		self.x_offset = x_off

		self.child_elements[0].move(0-self.x_offset, 0-self.y_offset)
		if(save_pos):
			self.scroll_vert_pos = y_off
			self.scroll_horiz_pos = x_off

	def _on_mouse_up(self, event):
		if event.button == 1:
			self.mouse_down = False
			self.dragging_horiz = False
			self.dragging_vert = False
			self.scroll_vert_pos = self.scroll_y
			self.scroll_horiz_pos = self.scroll_x

	def add(self, elem):
		self.handles_dirty = True
		if len(self.child_elements) > 0:
			raise ValueError("Scrollable can only contain one child element")
		container.add(self, elem)
		max_x_offset=0
		if len(self.child_elements) > 0:
			max_x_offset = self.child_elements[0].rect.w - self.rect.w
			if max_x_offset < 0:
				max_x_offset = 0
		self.max_x_offset = max_x_offset
		max_y_offset=0
		if len(self.child_elements) > 0:
			max_y_offset = self.child_elements[0].rect.h - self.rect.h
			if max_y_offset < 0:
				max_y_offset = 0
		self.max_y_offset = max_y_offset

		if self.width < self.child_elements[0].rect.w:
			self.show_horiz_multiplier = 1
		if self.height < self.child_elements[0].rect.h:
			self.show_vert_multiplier = 1

	def set_gui(self, gui):
		self.gui = gui
		for child in self.child_elements:
			child.set_gui(self.gui)
		self.eventmgr.bind(MOUSEBUTTONDOWN, self._on_mouse_event)
		self.eventmgr.bind(MOUSEBUTTONUP, self._on_mouse_up)
		self.bind("MOUSEOVER", self.hover)

	def set_target_surface(self, surface):
		container.set_target_surface(self, surface)
		for child in self.child_elements:
			child.set_target_surface(self.surf)

	def draw(self, events):
		self.surf.fill((0,0,0))
		self.setup_fg_image()
		for child in self.child_elements:
			child.draw(events)
		self.bg_color = (128, 128, 128, 128)
		if self.options.has_key("bg_color"):
			self.bg_color = self.options["bg_color"]
		self.fg_color = (0, 0, 0, 128)
		if self.options.has_key("fg_color"):
			self.fg_color = self.options["fg_color"]
		if self.options.has_key("scrollbar_width"):
			self.scrollbar_width = self.options["scrollbar_width"]
		self.draw_horiz_scrollbar()
		self.draw_vert_scrollbar()
		self.handles_dirty = False
		self.target_surface.blit(self.surf, self.rect)
	
	def get_focus_grid(self):
		return self.child_elements[0].get_focus_grid()

	def draw_vert_scrollbar(self):
		if self.child_elements[0].rect.h > self.rect.h:
			scrollbar_surf = pygame.Surface((self.scrollbar_width, self.rect.h-self.scrollbar_width*self.show_horiz_multiplier), pygame.locals.SRCALPHA)
			scrollbar_surf.fill(self.bg_color)
			self.surf.blit(scrollbar_surf, (self.rect.w-self.scrollbar_width, 0))

			handle_h = (self.rect.h**2 / self.child_elements[0].rect.h)
			if handle_h < self.scrollbar_width:
				handle_h = self.scrollbar_width
			handle_y_offset = 2
			handle_x_offset = 2
			if self.handles_dirty:
				handle_surf = pygame.Surface((self.scrollbar_width, handle_h), pygame.locals.SRCALPHA)
				if self.fg_image:
					if self.fg_image_nineslice:
						self.fg_image_nineslice.apply_to_surface(handle_surf)
					else:
						handle_h = self.fg_image.get_rect().h
						handle_surf = self.fg_image
				else:
					handle_surf.fill(self.fg_color, (2,2,self.scrollbar_width-4,handle_h-4))
				self.vert_handle_surf = handle_surf
			y_offset = 0
			if self.max_y_offset > 0:
				y_offset = (float(self.y_offset)/float(self.max_y_offset))*(self.rect.h-handle_h-self.scrollbar_width*self.show_horiz_multiplier)
			self.handle_y_offset = y_offset
				
			self.surf.blit(self.vert_handle_surf, (self.rect.w-self.scrollbar_width, y_offset))

	def draw_horiz_scrollbar(self):
		if self.child_elements[0].rect.w > self.rect.w:
			scrollbar_surf = pygame.Surface((self.rect.w-self.scrollbar_width*self.show_vert_multiplier, self.scrollbar_width), pygame.locals.SRCALPHA)
			scrollbar_surf.fill(self.bg_color)
			self.surf.blit(scrollbar_surf, (0, self.rect.h-self.scrollbar_width))

			handle_w = (self.rect.w**2 / self.child_elements[0].rect.w)
			handle_y_offset = 2
			handle_x_offset = 2
			if handle_w < self.scrollbar_width:
				handle_w = self.scrollbar_width
			if self.handles_dirty:
				handle_surf = pygame.Surface((handle_w, self.scrollbar_width), pygame.locals.SRCALPHA)
				if self.fg_image:
					if self.fg_image_nineslice:
						self.fg_image_nineslice.apply_to_surface(handle_surf)
					else:
						handle_w = self.fg_image.get_rect().w
						handle_surf = self.fg_image
				else:
					handle_surf.fill(self.fg_color, (2, 2, handle_w-4, self.scrollbar_width-4))
				self.horiz_handle_surf = handle_surf

			x_offset = 0
			if self.max_x_offset > 0:
				x_offset = (float(self.x_offset)/float(self.max_x_offset))*(self.rect.w-handle_w-self.scrollbar_width*self.show_vert_multiplier)
			self.handle_x_offset = x_offset
				
			self.surf.blit(self.horiz_handle_surf, (x_offset, self.rect.h-self.scrollbar_width))
	def setup_fg_image(self):
		image_path = ""
		if self.options.has_key("fg_image"):
			image_path = self.options["fg_image"]
		if image_path == self.fg_image_path:
			return

		self.fg_image = pygame.image.load(image_path)
		if self.options.has_key("fg_image_nineslice_radius"):
			self.fg_image_nineslice = Nineslice(self.fg_image, self.options["fg_image_nineslice_radius"])

	def handle_events(self, evs):
		if len(evs) < 1:
			return
		element.handle_events(self, evs)
		filtered_events = []
		window_rect = Rect(self.rect.left, self.rect.top, self.rect.w-self.scrollbar_width, self.rect.h-self.scrollbar_width)
		for ev in evs:
			if ev.type in [MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN]:
				if not window_rect.collidepoint(ev.pos):
					continue
			filtered_events.append(ev)
		for child in self.child_elements:
			child.handle_events(filtered_events)
