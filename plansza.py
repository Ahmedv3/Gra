import pygame
import sys
import random

class plansza(object):

    def __init__(self):
        """Konfiguracja, pętla główna, tytuł."""
        self.screen =  pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Plansza gry")
        self.size = self.screen.get_size()
        pygame.init()

        # kolory
        self.kolor_czarny = (0, 0, 0)

        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_l:
                    self.losowanie()
                    self.ruch()
                if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_SPACE:
                    self.rysuj()


    def rysuj(self):
        """Funkcja rysująca planszę."""

        #for i in range (1, 164, 41):
            #self.kwadrat = pygame.Rect(350+i ,300 , 40, 40)
            #self.pole=pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
            #self.pola.append(self.pole)
        #for i in range(1,164,41):
            #self.kwadrat = pygame.Rect(515, 301-i, 40, 40)
            #self.pole=pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
            #self.pola.append(self.pole)
        #for i in range(1,123,41):
            #self.kwadrat = pygame.Rect(475 - i, 177, 40, 40)
            #self.pole=pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
            #self.pola.append(self.pole)
        #print(self.pola)
        self.niebieski = ((0, 150, 255))
        self.czerwony = ((255, 0, 0))
        self.pola = []
        self.a = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(400, 170, 40, 40))
        self.pola.append(self.niebieski)
        self.b = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 170, 40, 40))
        self.pola.append(self.niebieski)
        self.c = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 211, 40, 40))
        self.pola.append(self.niebieski)
        self.d = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 252, 40, 40))
        self.pola.append(self.niebieski)
        self.e = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(400, 252, 40, 40))
        self.pola.append(self.niebieski)
        self.f = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(400, 293, 40, 40))
        self.pola.append(self.niebieski)
        self.g = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(400, 334, 40, 40))
        self.pola.append(self.niebieski)
        self.h = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 334, 40, 40))
        self.pola.append(self.niebieski)
        self.i = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(482, 334, 40, 40))
        self.pola.append(self.niebieski)
        self.j = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(482, 375, 40, 40))
        self.pola.append(self.niebieski)
        print(self.pola)

        pygame.display.flip()



    def losowanie(self):
        """Funkcja losująca liczbę od 1 do 6 i wyświetlająca ją na ekranie."""
        self.oczko = random.randint(1, 3)
        self.komunikat = str(self.oczko)
        self.komunikat2 = "<-- Twoja liczba. "
        self.czcionka = pygame.font.SysFont("dejavusans", 20)
        self.renderowanie_tekstu = self.czcionka.render(self.komunikat, 1, (250, 250, 250))
        self.renderowanie_tekstu2 = self.czcionka.render(self.komunikat2, 1, (250, 250, 250))
        self.zaslona = pygame.Rect(30, 550, 40, 40)
        pygame.draw.rect(self.screen, self.kolor_czarny, self.zaslona)
        self.zaslona_napis = pygame.Rect(60, 550, 165, 40)
        pygame.draw.rect(self.screen, self.kolor_czarny, self.zaslona_napis)
        self.screen.blit(self.renderowanie_tekstu, (30, 550))
        self.screen.blit(self.renderowanie_tekstu2, (60, 550))
        pygame.display.update()

    def ruch(self):
        """Funkcja wskazująca położenie pionka."""
        self.licznik = 0
        if self.oczko + self.licznik == 1:
            self.niebieski = self.czerwony
            self.a = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(400, 170, 40, 40))
            self.licznik += self.oczko
            pygame.display.update()
        elif self.oczko + self.licznik == 2:
            self.niebieski = self.czerwony
            self.b = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 170, 40, 40))
            self.licznik += self.oczko
            pygame.display.update()
        elif self.oczko + self.licznik == 3:
            self.niebieski = self.czerwony
            self.c = pygame.draw.rect(self.screen, self.niebieski, pygame.Rect(441, 211, 40, 40))
            self.licznik += self.oczko
            pygame.display.update()

if __name__ == '__main__':
    plansza()