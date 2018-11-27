from grid import *
from events import *
from event_manager import *
from nineslice import Nineslice
import gui
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

	event_type_bindings = None

	def __init__(self):
		self.options = {}
		self.options["focused"] = {}
		self.focus_grid = grid()
		self.focus_grid.set(0,0, self)
		self.eventmgr = event_manager()
		self.image_surfaces = {}
		self.id = gui.get_id(self)
		self.event_type_bindings = []

	def draw(self, events):
		opt_val = ""
		if self.options.has_key("image"):
			opt_val = self.options["image"]
		self.setup_state_image(opt_val)


	def setup_state_image(self, image_path, state="default"):
		if self.image_path == image_path:
			return
		self.image_path = image_path
		if not self.image_path:
			self.image_surfaces["default"] = None
			return

		image_surf = pygame.image.load(image_path)
		image_rect = image_surf.get_rect()
		self.image_surfaces[state] = image_surf
		
		if self.options.has_key("nineslice_radius"):
			radius = self.options["nineslice_radius"]
			self.image_surfaces[state] = pygame.Surface((self.rect.width, self.rect.height))
			nineslice = Nineslice(image_surf, self.options["nineslice_radius"])
			nineslice.apply_to_surface(self.image_surfaces[state])

	def remove_hover(self, event=None):
		pass

	def _callback(self, event, elem_id, callback):
		if event.elem.id != elem_id:
			return
		callback(event)

	def bind(self, event_type, callback):
		if not event_type in self.event_type_bindings:
			return
		f = lambda event: self._callback(event, self.id, callback)
		return self.eventmgr.bind(event_type, f)

	def unbind(self, callback_id):
		self.eventmgr.unbind(callback_id)

	def handle_events(self, events):
		if len(events) < 1:
			return
		self.eventmgr.run(events)

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
