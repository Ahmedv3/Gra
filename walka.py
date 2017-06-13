import pygame
import random
from pygame.locals import *

class Walka(object):

    def __init__(self):
        """Konstruktor inicjujący wartości początkowe dla przeciwnika i gracza."""
        self.hp = 100
        self.przeciwnik_hp = 100
        self.obrazenia_gracz = 0
        self.obrazenia_przeciwnik = 0


    def atak(self):
        """Funkcja ataku gracza zwracająca życie przeciwnika po wykonaniu ataku."""
        self.obrazenia_gracz = random.randint(10, 30)
        self.przeciwnik_hp -= self.obrazenia_gracz
        self.atak_przeciwnik()
        return self.przeciwnik_hp


    def atak_przeciwnik(self):
        """Funkcja ataku przeciwnika zwracająca życie gracza po wykonaniu ataku."""
        self.obrazenia_przeciwnik = random.randint(10, 30)
        self.hp -= self.obrazenia_przeciwnik
    #    print("przeciwnik {}".format(self.hp))
        return self.hp

    def kontynuacja(self,walka_status):
        """Funkcja wywoływana w przypadku wygranej gracza z przeciwnikiem, zerująca listę z współrzędnymi środków. """
        self.wspolrzedne_srodkow = []

    def przegrana(self):
        """Wywoływana w momencie przegranej gracza, wyswietlająca zdobyte zloto i komunikat."""
        self.screen.fill(self.black)
        pygame.display.flip()
        font = pygame.font.SysFont("dejavusans", 20)
        text = "Zostales zabity przez bandyte..."
        txt_rendering = font.render(text, 1, (250, 250, 250))
        self.screen.blit(txt_rendering, (100,200))
        text2 = "Zdobyles {} sztuk zlota.".format(self.gold)
        txt_rendering2 = font.render(text2, 1, (250, 250, 250))
        self.screen.blit(txt_rendering2, (100,300))
        text3 = "Wcisnij ESC by zakonczyc gre."
        txt_rendering3 = font.render(text3, 1, (250, 250, 250))
        self.screen.blit(txt_rendering3, (100,400))

        self.czaszka = pygame.image.load('czaszka.png')
        self.skull = pygame.display.get_surface()
        self.skull.blit(self.czaszka, (500,200))
        pygame.display.flip()


    def okno_walki(self,screen):
        """Funkcja czyszcząca ekran i przygotowująca scenerię walki, wyswietla komunikat oraz ustawia zycia przeciwnika i gracza na 100 """
        self.hp = 100
        self.przeciwnik_hp = 100
        self.screen.fill(self.black)
        font = pygame.font.SysFont("dejavusans", 20)
        plansza_walki = pygame.image.load('walka.png')
        plansza_walka = pygame.display.get_surface()
        plansza_walka.blit(plansza_walki, (0,0))
        pygame.display.flip()
    #    print("nastepuje okno walki")

        text = "Spotkales bandyte! Aby zaatakowac wcisnij klawisz: A"
        txt_rendering = font.render(text, 1, (250, 250, 250))
        self.screen.blit(txt_rendering, (30,50))
        pygame.display.flip()
        pass
