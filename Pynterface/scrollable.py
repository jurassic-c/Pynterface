import pygame
from events import *
from pygame.locals import *
from container import *

class scrollable(container):
	width = 0
	height = 0
	surf = None
	rect = None
	horiz_scrollbar_height = 0
	vert_scrollbar_width = 0
	y_offset = 0
	x_offset = 0
	max_y_offset = 0
	max_x_offset = 0
	def __init__(self, w, h):
		container.__init__(self)
		self.width = w
		self.height = h
		self.surf = pygame.Surface((w, h))
		self.rect = self.surf.get_rect()

	def mouse_event(self, event):
		y_off = self.y_offset
		x_off = self.x_offset
		scroll_multiplier=2
		if event.button == 4:
			y_off-=scroll_multiplier
		if event.button == 5:
			y_off+=scroll_multiplier
		if event.button == 6:
			x_off-=scroll_multiplier
		if event.button == 7:
			x_off+=scroll_multiplier

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

	def add(self, elem):
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
			self.horiz_scrollbar_height = 15
		if self.height < self.child_elements[0].rect.h:
			self.vert_scrollbar_width = 15

	def set_gui(self, gui):
		self.gui = gui
		for child in self.child_elements:
			child.set_gui(self.gui)
		gui.eventmgr.bind(MOUSEBUTTONDOWN, self.mouse_event)

	def set_target_surface(self, surface):
		container.set_target_surface(self, surface)
		for child in self.child_elements:
			child.set_target_surface(self.surf)

	def draw(self, events):
		self.surf.fill((0,0,0))
		for child in self.child_elements:
			child.draw(events)
		self.draw_horiz_scrollbar()
		self.draw_vert_scrollbar()
		self.target_surface.blit(self.surf, self.rect)
	
	def get_focus_grid(self):
		return self.child_elements[0].get_focus_grid()

	def draw_vert_scrollbar(self):
		if self.child_elements[0].rect.h > self.rect.h:
			scrollbar_surf = pygame.Surface((self.vert_scrollbar_width, self.rect.w-self.horiz_scrollbar_height), pygame.locals.SRCALPHA)
			scrollbar_surf.fill((128,128,128,128))
			self.surf.blit(scrollbar_surf, (self.rect.w-self.vert_scrollbar_width, 0))

			handle_h = (self.rect.h**2 / self.child_elements[0].rect.h)
			if handle_h < 15:
				handle_h = 15
			handle_surf = pygame.Surface((self.vert_scrollbar_width, handle_h), pygame.locals.SRCALPHA)
			handle_y_offset = 2
			handle_x_offset = 2
			handle_surf.fill((0,0,0,128), (2,2,self.vert_scrollbar_width-4,handle_h-4))
			y_offset = 0
			if self.max_y_offset > 0:
				y_offset = (float(self.y_offset)/float(self.max_y_offset))*(self.rect.h-handle_h-self.horiz_scrollbar_height)
				
			self.surf.blit(handle_surf, (self.rect.w-self.vert_scrollbar_width, y_offset))

	def draw_horiz_scrollbar(self):
		if self.child_elements[0].rect.w > self.rect.w:
			scrollbar_surf = pygame.Surface((self.rect.w-self.vert_scrollbar_width, self.horiz_scrollbar_height), pygame.locals.SRCALPHA)
			scrollbar_surf.fill((128,128,128,128))
			self.surf.blit(scrollbar_surf, (0, self.rect.h-self.horiz_scrollbar_height))

			handle_w = (self.rect.w**2 / self.child_elements[0].rect.w)
			if handle_w < self.horiz_scrollbar_height:
				handle_w = self.horiz_scrollbar_height
			handle_surf = pygame.Surface((handle_w, self.horiz_scrollbar_height), pygame.locals.SRCALPHA)
			handle_surf.fill((0,0,0,128), (2, 2, handle_w-4, self.horiz_scrollbar_height-4))
			x_offset = 0
			if self.max_x_offset > 0:
				x_offset = (float(self.x_offset)/float(self.max_x_offset))*(self.rect.w-handle_w-self.vert_scrollbar_width)
				
			self.surf.blit(handle_surf, (x_offset, self.rect.h-self.horiz_scrollbar_height))
