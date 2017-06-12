import pygame
import random
from pygame.locals import *

class Walka(object):

    def __init__(self):
        self.hp = 100
        self.przeciwnik_hp = 100
        self.obrazenia_gracz = 0
        self.obrazenia_przeciwnik = 0


    def atak(self):
        self.obrazenia_gracz = random.randint(10, 30)
        self.przeciwnik_hp -= self.obrazenia_gracz
        print(self.przeciwnik_hp)
        self.atak_przeciwnik()
        return self.przeciwnik_hp


    def atak_przeciwnik(self):
        self.obrazenia_przeciwnik = random.randint(5, 15)
        self.hp -= self.obrazenia_przeciwnik
        print("przeciwnik {}".format(self.hp))
        return self.hp

    def kontynuacja(self,walka_status):
        self.walka_status = False
        self.wspolrzedne_srodkow = []
        self.draw()
        return self.walka_status

    def przegrana(self):
        pass

    def okno_walki(self,screen):
        self.hp = 100
        self.przeciwnik_hp = 100
        self.screen.fill(self.black)
        font = pygame.font.SysFont("dejavusans", 20)
        plansza_walki = pygame.image.load('walka.png')
        plansza_walka = pygame.display.get_surface()
        plansza_walka.blit(plansza_walki, (0,0))
        pygame.display.flip()
        print("nastepuje okno walki")

        text = "Spotkales bandyte! Aby zaatakowac wcisnij klawisz: A"
        txt_rendering = font.render(text, 1, (250, 250, 250))
        self.screen.blit(txt_rendering, (30,50))
        pygame.display.flip()
        pass
