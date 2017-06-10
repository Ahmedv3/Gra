import pygame
import sys
import random
import time
from pygame.math import Vector2
from gracz import Player

class Plansza(Player):

    def __init__(self):
        self.resolution = (1280,720)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Knight And Magic 1.0")
        #self.size = self.screen.get_size()

        #self.clock = pygame.time.Clock()

        self.wspolrzedne_srodkow = []
        self.zdarzenia = []

        self.green = (0, 250, 0)
        self.blue = (0, 150, 255)
        self.black = (0, 0, 0)

        self.ruch = 0

        super().__init__()

        pygame.init()

    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit(0)
            elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_l:
                self.random(self.black)
                self.move(self.wspolrzedne_srodkow,self.ruch, self.green,self.black,self.screen)
                self.sprawdz_zdarzenia()
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_d:
                self.draw()

    def draw(self):
        for i in range(0, 440, 55):
            wsp_x = 200 + i
            wsp_y = 300
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)

        for j in range(0, 275, 55):
            wsp_x = 640
            wsp_y = 300 - j
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)

        for x in range(0,275,55):
            wsp_x = 640 + x
            wsp_y = 80
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        for a in range(0,385,55):
            wsp_x = 860
            wsp_y = 80 + a
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        for b in range(0,715,55):
            wsp_x = 860 - b
            wsp_y = 410
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        pygame.display.flip()


if __name__ == '__main__':

    plansza = Plansza()

    while True:
        plansza.events()
