class element:
	gui = None
	rect = None

	def __init__(self):
		pass

	def draw(self, events):
		pass

	def set_gui(self, gui):
		self.gui = gui

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def resize(self, w, h):
		self.rect.w = w
		self.rect.h = h