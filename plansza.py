import pygame
import sys
import random
from pygame.math import Vector2

class Plansza(object):

    def __init__(self):
        """Konfiguracja, pętla główna, tytuł."""
        self.resolution = (1280, 720)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Planszóweczka")
        self.size = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.wspolrzedne_srodkow = []
        self.ruch = 0
        self.zielony = (0, 250, 0)
        pygame.init()

        while True:
            self.events()

    def events(self):
        """Zdarzenia"""
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit(0)
            elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_l:
                self.random()
                self.move()
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_SPACE:
                self.draw()

    def draw(self):
        for i in range(0, 220, 55):
            self.wsp_x = 200 + i
            self.wsp_y = 300
            self.obiekt = Vector2(self.wsp_x, self.wsp_y)
            self.wspolrzedne_srodkow.append(self.obiekt)
            self.kwadrat = pygame.Rect(self.wsp_x,self.wsp_y, 50, 50)
            pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
        for j in range(0, 165, 55):
            self.wsp_x = 420
            self.wsp_y = 300 - j
            self.obiekt = Vector2(self.wsp_x, self.wsp_y)
            self.wspolrzedne_srodkow.append(self.obiekt)
            self.kwadrat = pygame.Rect(420, 300-j, 50, 50)
            pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
        print(self.wspolrzedne_srodkow)
        pygame.display.flip()

    def random(self):
        self.los = random.randint(1, 1)
        print(self.los)

    def move(self):

        self.tempRuch = self.ruch+self.los
        if self.tempRuch >= len(self.wspolrzedne_srodkow):
            self.tak = pygame.Rect(420, 190, 50, 50)
            self.pole1 = pygame.draw.rect(self.screen, self.zielony, self.tak)
            pygame.display.flip()
            print("przekroczony indeks tablicy")
            pass

        else:
            self.pole = self.wspolrzedne_srodkow[self.tempRuch]
            self.tak = pygame.Rect(self.pole.x, self.pole.y, 50, 50)
            pygame.draw.rect(self.screen, self.zielony, self.tak)
            pygame.display.flip()
            self.ruch = self.tempRuch
            print("krok")
        print("tempRuch:      ", self.tempRuch)


class Pawn(object):

    def __init__(self):
        pass

    def position_draw(self):

        pass


if __name__ == '__main__':
    Plansza()