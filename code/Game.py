#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        # Criate window
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        # For window to stay open
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()
            else:
                pass


