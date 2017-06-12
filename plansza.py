import pygame
import sys
import random
import time
from pygame.math import Vector2
from gracz import Player
from pygame.locals import *
from walka import Walka

class Plansza(Player):

    def __init__(self):
        self.resolution = (1280,720)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Knight And Magic 1.0")

        self.elfik = pygame.image.load('elf.png')
        self.tlo = pygame.display.get_surface()
        self.tlo2 = pygame.display.get_surface()
        self.tlo.blit(self.elfik, (15,0))
        self.logo = pygame.image.load('miecze_czarne.png')
        self.tlo2.blit(self.logo, (80,50))

        self.walka_status = False
        self.start = False

        self.wspolrzedne_srodkow = []
        self.zdarzenia = []

        self.green = (0, 250, 0)
        self.blue = (65, 34, 39)
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
                self.sprawdz_walke(self.screen,self.walka_status)
                self.sprawdz_zdarzenia(self.screen,self.black)
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_d:
                self.start = True
                self.draw()
            if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_a:
                if self.walka_status == True:
                    self.atak()
                    if self.przeciwnik_hp <= 0:
                        self.kontynuacja(self.walka_status)
                        print(self.walka_status)
                    elif self.hp <= 0:
                        print("zginales")
                else:
                    pass

    def draw(self):
        self.screen.fill(self.black)
        plansza_gry = pygame.image.load('plansza.png')
        plansza_tlo = pygame.display.get_surface()
        plansza_tlo.blit(plansza_gry, (15,0))
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
            wsp_x = 695 + x
            wsp_y = 80
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        for a in range(0,385,55):
            wsp_x = 915
            wsp_y = 135 + a
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        for b in range(0,715,55):
            wsp_x = 860 - b
            wsp_y = 465
            obiekt = Vector2(wsp_x, wsp_y)
            self.wspolrzedne_srodkow.append(obiekt)
            self.zdarzenia.append(obiekt)
            kwadrat = pygame.Rect(wsp_x, wsp_y, 50, 50)
            pygame.draw.rect(self.screen, self.blue, kwadrat)
        pygame.display.flip()
        print(self.wspolrzedne_srodkow)

    def ekran_startowy(self):
        for h in range(0,1250,55):
            wsp_x = 10 + h
            wsp_y = 5
            tlo = pygame.Rect(wsp_x,wsp_y,50,50)
            pygame.draw.rect(self.screen,(198,166,100), tlo)
        for m in range(0,1250,55):
            wsp_x = 10 + m
            wsp_y = 650
            tlo = pygame.Rect(wsp_x,wsp_y,50,50)
            pygame.draw.rect(self.screen,(198,166,100), tlo)
        for o in range(0,550,55):
            wsp_x = 10
            wsp_y = 80 + o
            tlo = pygame.Rect(wsp_x,wsp_y,50,50)
            pygame.draw.rect(self.screen,(198,166,100), tlo)
        for p in range(0,550,55):
            wsp_x = 1220
            wsp_y = 80 + p
            tlo = pygame.Rect(wsp_x,wsp_y,50,50)
            pygame.draw.rect(self.screen,(198,166,100), tlo)
        font = pygame.font.SysFont("dejavusans", 20)
        text = "Wcisnij d aby rozpoczac gre!"
        txt_rendering = font.render(text, 1, (250, 250, 250))
        self.screen.blit(txt_rendering, (150,320))
        pygame.display.flip()

if __name__ == '__main__':

    plansza = Plansza()

    while True:

        if plansza.start == False:
            plansza.ekran_startowy()
            plansza.events()
        else:
            plansza.events()
