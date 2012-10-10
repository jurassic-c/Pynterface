Pynterface
==========

Pynterface is an interface library for python, designed to be used with PyGame. Pynterface does not provide a collection of UI elements, such as buttons, dropdown boxes or input fields. Rather it provides the framework for the behavior of those elements, such as hovering, clicking, positioning and transitions as well as predifined behavior for interaction with keyboards and joysticks. Using Pynterface as a base, you can build your own UI toolkit without having to reinvent common behaviors. Being built with PyGame in mind, Pynterface will plug right into your existing game loop with very little hassle.

Dependencies
------------
 - Python 2.7
 - Pygame 1.9

Installation
------------

	$ git clone https://github.com/jurassic-c/Pynterface.git
	$ cp -r Pynterface/Pynterface /path/to/my/project/

Bugs and Issues
---------------

Please report all bugs and issues to the [issue tracker][1] for this project.


Contributing
------------

1. Fork it.
2. Create a branch (`git checkout -b my_markup`)
3. Commit your changes (`git commit -am "Added Snarkdown"`)
4. Push to the branch (`git push origin my_markup`)
5. Open a [Pull Request][2]
6. Crack open a cold one and wait

Base Classes
------------

 - **element**: Base class for all other interface classes. Your custom UI elements should derive from this.
 - **clickable**: Adds click and double click functionality to an element. Add this as a parent class to your custom UI elements to make them clickable.
 - **hoverable**: Addes hover functionality to an element. Add this as a parent class to your UI elements to make them hoverable.
 - **container**: Contains any number of sub-elements.
 - **hbox**: Container which stacks its child elements horizontally. Derive from this class to make any element which has child elements, such as a dropdown box or scrolling nav.
 - **vbox**: Container which stacks its child elements vertically. Derive from this class to make any element which has child elements, such as a dropdown box or scrolling nav.
 - **gui**: Parent container for all elements.

Current Features and Functionality
----------------------------------

### Element ###
 - positioning relative to parent
 - *onFocus* and *onBlur* callbacks

### Clickable ###
 - Adjustable double click timeout
 - *press()* and *unpress()* methods to simulate a click
 - Callbacks for:
 - - onClick
 - - onDoubleClick
 - - onMouseDown
 - - onMouseUp

### Hoverable ###
 - Callbacks for:
 - - onMouseOver
 - - onMouseOut

### Container ###
 - Holds child elements
 - Overridable methods for finding elements to the left and right as well as above
and below a given child element.

### Hbox / Vbox ###
 - Padding

### Gui ###
 - Automatically handles tab order of elements in an intuitive manner
 - Automatically handles navigation up, down, left and right between elements

Examples
--------

Example button class, actually used in the development process and in other examples. It's obviously quite simple, having no text or graphics. It produces a simple rectangular box.


	from Pynterface import *
	import pygame

	class button(element, clickable, hoverable):
		filled = True

		def __init__(self, width, height, x=0, y=0):
			self.rect = pygame.Rect(x, y, width, height)
			element.__init__(self)
			clickable.__init__(self)
			hoverable.__init__(self)

		def draw(self, events):
			rectSurf = pygame.Surface((self.rect.w, self.rect.h))
			width = 0
			if not self.filled:
				width = 1

			color = (122, 0, 0)
			if self.options.has_key("color"):
				color = self.options["color"]
			if self.focused:
				if self.options["focused"].has_key("color"):
					color = self.options["focused"]["color"]
			if self.hover and self.options["hover"].has_key("color"):
				color = self.options["hover"]["color"]
			if self.pressed:
				if self.options["pressed"].has_key("color"):
					color = self.options["pressed"]["color"]
			pygame.draw.rect(rectSurf, color, pygame.Rect(0, 0, self.rect.width, self.rect.height), width)
			self.gui.surface.blit(rectSurf, self.rect)

			element.draw(self, events)
			clickable.draw(self, events)
			hoverable.draw(self, events)


[1]: https://github.com/jurassic-c/Pynterface/issues
[2]: http://github.com/github/markup/pulls