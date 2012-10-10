import pygame, sys
from button import *
from pygame.locals import *

from Pynterface import *

def rollover(elem, event):
	elem.color = (122, 122, 122)

def rollout(elem, event):
	elem.color = (122, 0, 0)

def mousedown(elem, event):
	pass

def mouseup(elem, event):
	pass

def doclick(elem, event):
	print "CLICK"

def doubleclick(elem, event):
	if elem.filled:
		elem.filled = False
	else:
		elem.filled = True

def focus(elem):
	pass

def blur(elem):
	pass

def get_button(w, h, color=(122,0,0)):
	bttn = button(w, h)
	bttn.onMouseOver = rollover
	bttn.onMouseOut = rollout
	bttn.onMouseDown = mousedown
	bttn.onMouseUp = mouseup
	bttn.onClick = doclick
	bttn.onDoubleClick = doubleclick
	bttn.onFocus = focus
	bttn.onBlur = blur
	bttn.options["color"] = color
	bttn.options["focused"]["color"] = (122, 50, 50)
	bttn.options["pressed"]["color"] = (0, 0, 122)
	bttn.options["hover"]["color"] = (0, 0, 255)
	return bttn

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((540,430))

guiObj = gui.gui(window)

main_hb = hbox()
main_hb.padding = 10

vb = vbox()
vb.padding = 10

hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

vb.add(get_button(320, 100))

hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

vb.add(get_button(320, 100))
main_hb.add(vb)

vb = vbox()
vb.padding = 10

hb = hbox()
hb.padding = 10
hb.add(get_button(100,100))
hb.add(get_button(100,100))
vb.add(hb)

hb = hbox()
hb.padding = 10

hb.add(get_button(100, 320))

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