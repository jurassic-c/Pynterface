import pygame, sys
from button import *
from text_field import *
from pygame.locals import *
from Pynterface.events import *

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
	print "CLICK: %d" % event.elem.id

def doubleclick(event):
	print "DOUBLE CLICK %d" % event.elem.id
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
	bttn.bind("MOUSEOVER", rollover)
	bttn.bind("MOUSEOUT", rollout)
	bttn.bind("MOUSEBUTTONDOWN", mousedown)
	bttn.bind("MOUSEBUTTONUP", mouseup)
	bttn.bind("CLICK", doclick)
	bttn.bind("DOUBLECLICK", doubleclick)
	bttn.bind("FOCUS", focus)
	bttn.bind("BLUR", blur)
	bttn.options["image"] = "assets/button.png";
	bttn.options["hover"]["image"] = "assets/button_hover.png";
	bttn.options["pressed"]["image"] = "assets/button_pressed.png";
	bttn.options["focused"]["image"] = "assets/button_focused.png";
	bttn.options["nineslice_radius"] = 5
	bttn.options["text"] = "Button ID: %d" % bttn.id
	bttn.options["font_size"] = 15
	bttn.options["text_color"] = (0,0,255, 128)
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

scroll = scrollable(250,250)
scroll.options["bg_color"] = (128,128,128,128)
scroll.options["fg_image"] = "assets/scroll_handle.png"
scroll.options["fg_image_nineslice_radius"] = 6
scroll.add(main_hb)

main_vb = vbox()
main_vb.padding = 10
main_vb.add(scroll)

text_hb = hbox()
text_hb.padding = 10
text = text_field(200, 30)
text.options["color"] = (122,122,122,122)
text.options["text_color"] = (0,0,0)
text.options["font_size"] = 20
text.options["text_position"] = "left"
text.options["horizontal_padding"] = 10
text.options["max_width"] = 200

def clear_txt(ev=None):
	text.value = ""

def update_label(ev=None):
	print "UPDATING LABEL"
	bttn_seven = guiObj.get_element(7)
	bttn_seven.options["text"] = text.value
text.bind("CHANGE", update_label)

clear_btn = get_button(80, 30)
clear_btn.options["text"] = "Clear"
clear_btn.bind("CLICK", clear_txt)

text_hb.add(text)
text_hb.add(clear_btn)
main_vb.add(text_hb)

guiObj.add(main_vb)

frame_time = 0

pygame.key.set_repeat(100)
while True:
	events = pygame.event.get()
	pygame.event.clear()
	guiObj.draw(events, frame_time)
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	frame_time = fpsClock.tick(60)
