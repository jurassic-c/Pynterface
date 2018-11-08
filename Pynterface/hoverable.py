import pygame
from events import *
from pygame.locals import *

class hoverable:
	rect = None
	hover = False
	last_hover = False
	hover_enabled = True

	def __init__(self):
		self.options["hover"] = {}

	def set_gui(self, gui):
		gui.bind(MOUSEMOTION, self._on_mousemotion)

	def draw(self, events):
		pass

	def mouse_over(self, event):
		if self.hover and not self.last_hover:
			self.eventmgr.run([pygame.event.Event(MOUSEOVER, {"elem": self, "pos":self.gui.mouse_pos})])

	def mouse_out(self, event):
		if not self.hover and self.last_hover:
			self.eventmgr.run([pygame.event.Event(MOUSEOUT, {"elem": self, "pos":self.gui.mouse_pos})])

	def _on_mousemotion(self, event):
		if not self.hover_enabled:
			self.hover = False
			return
		if event.type == MOUSEMOTION:
			if self.rect.collidepoint(event.pos):
				self.hover = True
			else:
				self.hover = False
			self.mouse_over(event)
			self.mouse_out(event)
			self.last_hover = self.hover
