class grid:
	w = 0
	h = 0
	grid = None

	def __init__(self):
		rows = grid_array()
		rows.onAdd = self._add_width
		cols = grid_array()
		cols.onAdd = self._add_height
		self.grid = rows
		self.grid.append(cols)

	def __getitem__(self, x):
		return self.grid[x]

	def __setitem__(self, x, value):
		self.grid[x] = value

	def __str__(self):
		return str(self.grid)

	def item(self, coords):
		return self.grid[coords[0]][coords[1]]

	def set(self, x, y, value):
		if x > self.w -1:
			self._expand(x+1, self.h)
		if y > self.h -1:
			self._expand(self.w, y+1)
		self.grid[x][y] = value

	def next_coords_from(self, start, direction="right"):
		x, y = start

		if direction == "right":
			x+= 1
			if x >= self.w:
				x = 0
		elif direction == "left":
			x-= 1
			if x < 0:
				x = self.w-1
		elif direction == "up":
			y-= 1
			if y < 0:
				y = self.h-1
		elif direction == "down":
			y+= 1
			if y >= self.h:
				y = 0
		return (x, y)

	def append(self, value):
		self.grid.append(grid_array(value))

	def add_right(self, new_grid):
		w = self.w
		for y in range(new_grid.h):
			for x in range(new_grid.w):
				self.set(x+w, y, new_grid[x][y])

	def add_bottom(self, new_grid):
		h = self.h
		for x in range(new_grid.w):
			for y in range(len(new_grid[x])):
				self.set(x, y+h, new_grid[x][y])

	def _expand(self, w, h):
		if w > self.w:
			for i in range(w - self.w):
				self.grid.append(grid_array())
		for col in self.grid:
			for i in range(h - len(col)):
				col.append(None)
		self.h = h

	def get_col(self, x):
		return self.grid[x]

	def get_row(self, y):
		new_row = grid_array()
		for x in range(self.w):
			new_row.append(self.grid[x][y])
		return new_row

	def _add_width(self, arr):
		self.w+= 1

	def _add_height(self, arr):
		if len(arr) > self.h:
			self.h = len(arr)

class grid_array:
	items = None
	onAdd = None

	def __init__(self, value=None):
		self.items = []
		if isinstance(value, list):
			self.items.extend(value)
		elif value != None:
			self.items.append(value)

	def __getitem__(self, i):
		return self.items[i]

	def __setitem__(self, i, value):
		self.items[i] = value

	def __len__(self):
		return len(self.items)

	def append(self, value):
		self.items.append(value)
		if self.onAdd:
			self.onAdd(self)

	def unique(self):
	    seen = set()
	    seen_add = seen.add
	    return [ x for x in self.items if x not in seen and not seen_add(x)]

	def __str__(self):
		return "[%s]" % ', '.join([str(item) for item in self.items])