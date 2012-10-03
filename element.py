class element:
	gui = None
	rect = None
	state = ""
	parent = None
	id = 0

	options = None

	focused = False
	onFocus = None
	onBlur = None

	def __init__(self):
		self.options = {"focused": {}}

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

	def focus(self, options={}):
		if not self.focused and self.onFocus:
			self.onFocus(self)
		self.focused = True
		self.parent.set_focus(self.id)
		self.gui.set_focus(self.id)

	def blur(self):
		if self.focused and self.onBlur:
			self.onBlur(self)
		self.focused = False

	def element_right(self):
		return self.parent.element_right(self.id)

	def element_left(self):
		return self.parent.element_left(self.id)

	def element_above(self):
		return self.parent.element_above(self.id)

	def element_below(self):
		return self.parent.element_below(self.id)