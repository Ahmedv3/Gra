import pygame
from pygame.math import Vector2
import random
from walka import Walka

class Player(Walka):

    def __init__(self):
        self.gold = 0
        self.losowe_zdarzenia = random.randint(20, 35)
        self.zloto = random.randint(50, 1000)
        self.tempRuch = 0
        print(self.losowe_zdarzenia)
        self.punkty_walk = [Vector2((310,300)),Vector2((365,300)),Vector2((420,300)),Vector2((530,300)),Vector2((640,135)),Vector2((640,80))]
        super().__init__()

    def random(self,black):
        font = pygame.font.SysFont("dejavusans", 20)
        self.los = random.randint(1, 1)
        text = str(self.los)
        text2 = "Twoja liczba to: "
        txt_rendering = font.render(text, 1, (250, 250, 250))
        txt_rendering2 = font.render(text2, 1, (250, 250, 250))
        zaslona = pygame.Rect(30, 650, 40, 40)
        zaslona_napis = pygame.Rect(60, 650, 165, 40)
        pygame.draw.rect(self.screen, self.black, zaslona)
        pygame.draw.rect(self.screen, self.black, zaslona_napis)
        self.screen.blit(txt_rendering2, (30, 650))
        self.screen.blit(txt_rendering, (190, 650))
        pygame.display.flip()

    def move(self,wspolrzedne_srodkow,green,ruch,black,screen):

        self.tempRuch = self.ruch + self.los
        if self.tempRuch >= len(self.wspolrzedne_srodkow):
            pionek = pygame.Rect(200, 465, 50, 50)
            pygame.draw.rect(self.screen, self.green, pionek)
            self.wspolrzedne_srodkow.append(Vector2((200,465)))
            self.ruch = self.tempRuch
            self.screen.fill(self.black)
            pass

        else:
            self.pole = self.wspolrzedne_srodkow[self.tempRuch]
            figura = pygame.Rect(self.pole.x, self.pole.y, 50, 50)
            pygame.draw.rect(self.screen, self.green, figura)
            self.ruch = self.tempRuch
        pygame.display.flip()

    def sprawdz_zdarzenia(self,screen,black):
        zloto = random.randint(50, 1000)
        zaslona = pygame.Rect(270, 650, 600, 40)
        zaslona2 = pygame.Rect(970, 650, 200, 40)
        font = pygame.font.SysFont("dejavusans", 20)
        text2 = "Twoje zloto: {}".format(self.gold)
        txt_rendering2 = font.render(text2, 1, (250, 250, 250))
        text = "Znalazles sakiewkę ze zlotem! Otrzymujesz {} szt. zlota!".format(zloto)
        txt_rendering = font.render(text, 1, (250, 250, 250))
        pygame.draw.rect(self.screen, self.black, zaslona)
        pygame.draw.rect(self.screen, self.black, zaslona2)
        for i in range(0,self.losowe_zdarzenia):
            if self.wspolrzedne_srodkow[i] == self.pole:

                self.screen.blit(txt_rendering, (300,650))
                self.gold += zloto
                self.screen.blit(txt_rendering2, (1000,650))
                pass
            else:
                self.screen.blit(txt_rendering2, (1000,650))
                pass

    def sprawdz_walke(self,screen,walka_status):
        if self.wspolrzedne_srodkow[2] == self.punkty_walk[0]:
            self.walka_status = True
            self.okno_walki(self.screen)
            pass
        #elif self.wspolrzedne_srodkow[3] == self.punkty_walk[1]:
        #    self.walka_status = True
        #    self.okno_walki(self.screen)
        #    pass
        #elif self.wspolrzedne_srodkow[4] == self.punkty_walk[2]:
        #    self.walka_status = True
        #    self.okno_walki(self.screen)
        #    pass
        #elif self.wspolrzedne_srodkow[6] == self.punkty_walk[3]:
        #    self.walka_status = True
        #    self.okno_walki(self.screen)
        #    pass
        #elif self.wspolrzedne_srodkow[11] == self.punkty_walk[4]:
        #    self.walka_status = True
        #    self.okno_walki(self.screen)
        #    pass

        else:
            pass
