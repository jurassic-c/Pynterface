import pygame, sys
from button import *
from pygame.locals import *

from Pynterface import *

def rollover(event):
	print "MOUSEOVER:", event.elem.id

def rollout(event):
	print "MOUSEOUT:", event.elem.id

def mousedown(event):
	pass

def mouseup(event):
	pass

def doclick(event):
	print "CLICK"

def doubleclick(event):
	elem = event.elem
	pinned = False
	if elem.options.has_key("pinned"):
		pinned = elem.options["pinned"]
	if pinned:
		elem.options["pinned"] = False
		elem.hover_enabled = True
		elem.options["image"] = "assets/button.png"
		elem.options["focused"]["image"] = "assets/button_focused.png"
	else:
		elem.options["pinned"] = True
		elem.hover_enabled = False
		elem.hover = False
		elem.options["image"] = "assets/button_pinned.png"
		elem.options["focused"]["image"] = "assets/button_pinned.png"

def focus(event):
	pass

def blur(event):
	pass

def get_button(w, h, color=(122,0,0)):
	bttn = button(w, h)
	bttn.bind(MOUSEOVER, rollover)
	bttn.bind(MOUSEOUT, rollout)
	bttn.bind(MOUSEBUTTONDOWN, mousedown)
	bttn.bind(MOUSEBUTTONUP, mouseup)
	bttn.bind(CLICK, doclick)
	bttn.bind(DOUBLECLICK, doubleclick)
	bttn.bind(FOCUS, focus)
	bttn.bind(BLUR, blur)
	bttn.options["image"] = "assets/button.png";
	bttn.options["hover"]["image"] = "assets/button_hover.png";
	bttn.options["pressed"]["image"] = "assets/button_pressed.png";
	bttn.options["focused"]["image"] = "assets/button_focused.png";
	bttn.options["nineslice_radius"] = 5
	bttn.options["text"] = "Test Message"
	bttn.options["font_size"] = 20
#	bttn.options["color"] = color
#	bttn.options["focused"]["color"] = (122, 50, 50)
#	bttn.options["pressed"]["color"] = (0, 0, 122)
#	bttn.options["hover"]["color"] = (0, 0, 0, 0)
#	bttn.options["focused"]["image"] = (122, 50, 50)
#	bttn.options["pressed"]["color"] = (0, 0, 122)
#	bttn.options["hover"]["color"] = (0, 0, 0, 0)
	return bttn

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((540,430))

guiObj = gui.gui(window)

#H0
main_hb = hbox()
main_hb.padding = 10

#V1
vb = vbox()
vb.padding = 10

#H2
hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

#B6
vb.add(get_button(320, 100))

#H7
hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

#B11
vb.add(get_button(320, 100))
main_hb.add(vb)

#V12
vb = vbox()
vb.padding = 10

#H13
hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

#H16
hb = hbox()
hb.padding = 10

#B17
hb.add(get_button(100, 320))

#V18
vb2 = vbox()
vb2.padding = 10
vb2.add(get_button(100,100))
vb2.add(get_button(100,100))
vb2.add(get_button(100,100))
hb.add(vb2)

vb.add(hb)
main_hb.add(vb)

guiObj.add(main_hb)

frame_time = 0

while True:
	events = pygame.event.get()
	guiObj.draw(events, frame_time)
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	frame_time = fpsClock.tick(60)
