#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Menu import Menu

import pygame

class Game:

    def __init__(self):
        self.window = None
        pygame.init()
        # Criate window
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        # For window to stay open
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit() # Close Window
            #        quit() # End pygame
