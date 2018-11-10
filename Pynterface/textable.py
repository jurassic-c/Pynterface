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
            font_path = None
            font_size = 10
            text_color = None
            if self.options.has_key("font_path"):
                font_path = self.options["font_path"]
            if self.options.has_key("font_size"):
                font_size = self.options["font_size"]
            if self.options.has_key("text_color"):
                text_color = self.options["text_color"]
            self.font = pygame.freetype.Font(font_path, size=font_size)
            if text_color:
                self.font.fgcolor = text_color
        opt_text = ""
        if self.options.has_key("text"):
            opt_text = self.options["text"]
        if opt_text != self.text:
            self.text_surf, self.text_rect = self.font.render(opt_text)
        self.text = opt_text

    def get_text_position_rect(self, image_surf, target_rect, position="center"):
            top = 0
            left = 0
            image_rect = image_surf.get_rect()
            if position == "top_left":
                    left = 0
                    top = 0
            elif position == "top":
                    left = (target_rect.width - image_rect.w) / 2
                    top = 0
            elif position == "top_right":
                    left = target_rect.width - image_rect.w
                    top = 0
            elif position == "left":
                    left = 0
                    top = (target_rect.height - image_rect.h) / 2
            elif position == "center":
                    left = (target_rect.width - image_rect.w) / 2
                    top = (target_rect.height - image_rect.h) / 2
            elif position == "right":
                    left = (target_rect.width - image_rect.w)
                    top = (target_rect.height - image_rect.h) / 2
            elif position == "bottom_left":
                    left = 0
                    top = target_rect.height - image_rect.h
            elif position == "bottom":
                    left = (target_rect.width - image_rect.w) / 2
                    top = target_rect.height - image_rect.h
            elif position == "bottom_right":
                    left = target_rect.width - image_rect.w
                    top = target_rect.height - image_rect.h
            return (left, top)
