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
        """Konstruktor inicjujący ustawienia początkowe, rysujący tło i ekran poczatkowy."""
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
        self.plansza=pygame.image.load('plansza.png')
        self.plansza_tlo = pygame.display.get_surface()
        self.ruch = 0

        super().__init__()



        pygame.init()

    def events(self):
        """Funkcja obsługi klawiszy"""
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
                    self.kontynuacja(self.walka_status)
                    self.atak()
                    zaslona = pygame.Rect(45, 620, 350, 100)
                    font = pygame.font.SysFont("dejavusans", 20)
                    text = "Zadales {} obrazen bandycie.".format(self.obrazenia_gracz)
                    txt_rendering = font.render(text, 1, (250, 250, 250))
                    text2 = "Bandyta zadal ci {} obrazen.".format(self.obrazenia_przeciwnik)
                    txt_rendering2 = font.render(text2, 1, (250, 250, 250))
                    pygame.draw.rect(self.screen, self.black, zaslona)
                    self.screen.blit(txt_rendering, (50,625))
                    self.screen.blit(txt_rendering2, (50,670))
                    pygame.display.flip()
                    if self.przeciwnik_hp <= 0:
                        self.walka_status=False
                        self.draw()
                        self.move(self.wspolrzedne_srodkow,self.ruch, self.green,self.black,self.screen)
                    elif self.hp <= 0:
                        self.przegrana()
                else:
                    #print("wyszedłem")
                    pass

    def draw(self):
        """Funkcja rusyjąca planszę."""

        self.plansza_tlo.blit(self.plansza, (15,0))
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

        pygame.display.update()

    def ekran_startowy(self):
        """Funkcja rysująca ekran startowy."""
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
