#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.Const import WINDOW_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTIONS, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Carregou a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # Criou o retângulo

    def run(self, ):
        menu_option = 0 # Starts on zero - first option
        # Carrega a música e a imagem apenas uma vez antes do loop
        pygame.mixer_music.load('asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # - 1 é para tocar em loop

        while True:
            # 1. Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Down Key
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP: # Up Key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN: # Enter
                        return MENU_OPTIONS[menu_option]


            # 2. Draw window elements
            self.window.blit(source=self.surf, dest=self.rect)  # Informou que a imagem deve aparecer no retângulo
            self.menu_text(text_size=70, text="Mountain", text_color=COLOR_ORANGE,
                           text_center_pos=((WINDOW_WIDTH / 2), 70))
            self.menu_text(text_size=70, text="Shooter", text_color=COLOR_ORANGE,
                           text_center_pos=((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(text_size=30, text=MENU_OPTIONS[i], text_color=COLOR_YELLOW,
                               text_center_pos=((WINDOW_WIDTH / 2), 175 + 25 * i))
                else:
                    self.menu_text(text_size=30, text=MENU_OPTIONS[i], text_color=COLOR_WHITE,
                                  text_center_pos=((WINDOW_WIDTH / 2), 175 + 25 * i))

            pygame.display.flip()  # Atualiza a tela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
