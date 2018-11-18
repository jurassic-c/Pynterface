from grid import *
from events import *
from event_manager import *
from nineslice import Nineslice
import pygame.event
import pygame.image
import pygame.rect

class element:
	gui = None
	rect = None
	state = ""
	parent = None
	local_x = 0
	local_y = 0
	id = 0
	eventmgr = None
	image_surf = None
	image_rect = None
	image_surfaces = None
	image_path = ""
	target_surface = None

	options = None

	focused = False

	focus_grid = None
	focus_coords = None

	tab_order = 0

	def __init__(self):
		self.options = {}
		self.options["focused"] = {}
		self.focus_grid = grid()
		self.focus_grid.set(0,0, self)
		self.eventmgr = event_manager()
		self.image_surfaces = {}

	def draw(self, events):
		self.setup_default_image()


	def setup_default_image(self):
		opt_val = ""
		if self.options.has_key("image"):
			opt_val = self.options["image"]
		if self.image_path == opt_val:
			return
		self.image_path = self.options["image"]
		if not self.image_path:
			self.image_surfaces["default"] = None
			return

		image_surf = pygame.image.load(self.options["image"])
		image_rect = image_surf.get_rect()
		self.image_surfaces["default"] = image_surf
		
		if self.options.has_key("nineslice_radius"):
			radius = self.options["nineslice_radius"]
			self.image_surfaces["default"] = pygame.Surface((self.rect.width, self.rect.height))
			nineslice = Nineslice(image_surf, self.options["nineslice_radius"])
			nineslice.apply_to_surface(self.image_surfaces["default"])


	def bind(self, event, callback):
		return self.eventmgr.bind(event, callback)

	def unbind(self, callback_id):
		self.eventmgr.unbind(callback_id)

	def set_gui(self, gui):
		self.gui = gui

	def set_target_surface(self, surface):
		self.target_surface = surface

	def move(self, x, y):
		self.local_x = x
		self.local_y = y
		if self.parent:
			x = self.parent.rect.x + self.local_x
			y = self.parent.rect.y + self.local_y
		self.rect.x = x
		self.rect.y = y

	def resize(self, w, h):
		self.rect.w = w
		self.rect.h = h

	def focus(self, options={}):
		if not self.focused:
			self.eventmgr.run([pygame.event.Event(FOCUS, {"elem": self})])
		self.focused = True
		self.parent.set_focus(self.id)

	def blur(self):
		if self.focused:
			self.eventmgr.run([pygame.event.Event(BLUR, {"elem": self})])
		self.focused = False

	def element_right(self):
		return self.parent.element_right(self.id)

	def element_left(self):
		return self.parent.element_left(self.id)

	def element_above(self):
		return self.parent.element_above(self.id)

	def element_below(self):
		return self.parent.element_below(self.id)

	def get_focus_grid(self):
		return self.focus_grid
