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


        # kolory
        self.zielony = (0, 250, 0)
        self.niebieski = (0, 150, 255)
        self.czarny = (0, 0, 0)

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
        for i in range(0, 440, 55):
            self.wsp_x = 200 + i
            self.wsp_y = 300
            self.obiekt = Vector2(self.wsp_x, self.wsp_y)
            self.wspolrzedne_srodkow.append(self.obiekt)
            self.kwadrat = pygame.Rect(self.wsp_x, self.wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.niebieski, self.kwadrat)
        for j in range(0, 275, 55):
            self.wsp_x = 640
            self.wsp_y = 300 - j
            self.obiekt = Vector2(self.wsp_x, self.wsp_y)
            self.wspolrzedne_srodkow.append(self.obiekt)
            self.kwadrat = pygame.Rect(self.wsp_x, self.wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.niebieski, self.kwadrat)
        print(self.wspolrzedne_srodkow)
        pygame.display.flip()

    def random(self):
        self.los = random.randint(1, 6)
        self.text = str(self.los)
        self.text2 = "Twoja liczba to: "
        self.font = pygame.font.SysFont("dejavusans", 20)
        self.txt_rendering = self.font.render(self.text, 1, (250, 250, 250))
        self.txt_rendering2 = self.font.render(self.text2, 1, (250, 250, 250))
        self.zaslona = pygame.Rect(30, 550, 40, 40)
        pygame.draw.rect(self.screen, self.czarny, self.zaslona)
        self.zaslona_napis = pygame.Rect(60, 550, 165, 40)
        pygame.draw.rect(self.screen, self.czarny, self.zaslona_napis)
        self.screen.blit(self.txt_rendering2, (30, 550))
        self.screen.blit(self.txt_rendering, (190, 550))
        print(self.los)

    def move(self):

        self.tempRuch = self.ruch + self.los
        if self.tempRuch >= len(self.wspolrzedne_srodkow):
            self.tak = pygame.Rect(640, 80, 50, 50)
            self.pole1 = pygame.draw.rect(self.screen, self.zielony, self.tak)
            pygame.display.flip()
            print("przekroczony indeks tablicy")
            self.ruch = self.tempRuch
            pass

        else:
            self.pole = self.wspolrzedne_srodkow[self.tempRuch]
            self.figura = pygame.Rect(self.pole.x, self.pole.y, 50, 50)
            pygame.draw.rect(self.screen, self.zielony, self.figura)
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