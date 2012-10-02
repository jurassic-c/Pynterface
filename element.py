class element:
	gui = None
	rect = None
	state = None
	parent = None
	id = 0

	has_focus = False
	onFocus = None
	onBlur = None

	def __init__(self):
		pass

	def draw(self, events):
		pass

	def set_gui(self, gui):
		self.gui = gui
		if not self.id:
			self.id = self.gui.register_element(self)

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def resize(self, w, h):
		self.rect.w = w
		self.rect.h = h

	def focus(self):
		if not self.has_focus and self.onFocus:
			self.onFocus(self)
		self.has_focus = True
		self.gui.set_focus(self.id)

	def blur(self):
		if self.has_focus and self.onBlur:
			self.onBlur(self)
		self.has_focus = False