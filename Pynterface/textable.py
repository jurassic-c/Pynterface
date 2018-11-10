import pygame
from events import *
from pygame.locals import *

class textable:
    text = ""
    font = None
    text_surf = None
    text_rect = None
    def __init__(self):
        pass

    def set_gui(self, gui):
        self.gui = gui

    def draw(self, events):
        if not self.font:
            font_name = None
            font_size = 10
            if self.options.has_key("font_name"):
                font_name = self.options["font_name"]
            if self.options.has_key("font_size"):
                font_size = self.options["font_size"]
            self.font = pygame.freetype.Font(font_name, size=font_size)
        opt_text = ""
        if self.options.has_key("text"):
            opt_text = self.options["text"]
        if opt_text != self.text:
            self.text_surf, self.text_rect = self.font.render(opt_text)
        self.text = opt_text
