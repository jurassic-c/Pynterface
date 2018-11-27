import pygame
from pygame import locals

pface_event = locals.USEREVENT

CLICK = pface_event + 1
DOUBLECLICK = pface_event + 2
MOUSEOVER = pface_event + 3
MOUSEOUT = pface_event + 4
DWELLCLICK = pface_event + 5
DRAG = pface_event + 6
FOCUS = pface_event  + 7
BLUR = pface_event + 8
