#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Menu import Menu
from code.Const import WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        # Criate window
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        # For window to stay open
        while True:
            menu = Menu(self.window)
            menu.run()
            pass