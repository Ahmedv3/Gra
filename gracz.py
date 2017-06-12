import pygame
from pygame.math import Vector2
import random
from walka import Walka

class Player(Walka):

    def __init__(self):
        self.gold = 0
        self.losowe_zdarzenia = random.randint(7, 15)
        self.zloto = random.randint(50, 1000)
        self.tempRuch = 0
    #    print(self.losowe_zdarzenia)
        self.punkty_walk = [Vector2((310,300)),Vector2((365,300)),Vector2((420,300)),Vector2((530,300)),Vector2((640,135)),Vector2((640,80))]
        super().__init__()

    def random(self,black):
        font = pygame.font.SysFont("dejavusans", 20)
        self.los = random.randint(1, 6)
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
        #print(len(self.wspolrzedne_srodkow),"  " , self.tempRuch)
        if self.tempRuch >= len(self.wspolrzedne_srodkow):
            self.koniec = True
            self.walka_status=False
        #    print("Pierwszy if")
            pionek = pygame.Rect(200, 465, 50, 50)
            pygame.draw.rect(self.screen, self.green, pionek)
            self.wspolrzedne_srodkow.append(Vector2((200,465)))
            self.ruch = self.tempRuch
            self.screen.fill(self.black)
            pygame.display.flip()

            self.elfik = pygame.image.load('elf.png')
            self.tlo = pygame.display.get_surface()
            self.tlo2 = pygame.display.get_surface()
            self.tlo.blit(self.elfik, (15,0))
            self.logo = pygame.image.load('miecze_czarne.png')
            self.tlo2.blit(self.logo, (80,50))
            font = pygame.font.SysFont("dejavusans", 20)
            text = "Gratulacje! Ukonczyles gre! Wcisnij ESC zeby wyjsc. "
            txt_rendering = font.render(text, 1, (250, 250, 250))
            self.screen.blit(txt_rendering, (50,290))

            pygame.display.flip()

            #print("narysowałem czarne tło")
        else:
            self.pole = self.wspolrzedne_srodkow[self.tempRuch]
            figura = pygame.Rect(self.pole.x, self.pole.y, 50, 50)
            pygame.draw.rect(self.screen, self.green, figura)
        #    print("SELF RUCH",self.ruch)
            self.ruch = self.tempRuch
            self.los =0
            pygame.display.flip()

    def sprawdz_zdarzenia(self,screen,black):
        zloto = random.randint(50, 1000)
        zaslona = pygame.Rect(300, 650, 720, 40)
        zaslona2 = pygame.Rect(1000, 650, 200, 40)
        font = pygame.font.SysFont("dejavusans", 20)
        text2 = "Twoje zloto: {}".format(self.gold)
        txt_rendering2 = font.render(text2, 1, (250, 250, 250))
        text = "Znalazles sakiewkę ze zlotem! Otrzymujesz {} szt. zlota!".format(zloto)
        txt_rendering = font.render(text, 1, (250, 250, 250))
        pygame.draw.rect(self.screen, self.black, zaslona)
        pygame.draw.rect(self.screen, self.black, zaslona2)
        for i in range(0,self.losowe_zdarzenia):
            if self.wspolrzedne_srodkow[i] == self.pole:

                self.screen.blit(txt_rendering, (500,650))
                self.gold += zloto
                self.screen.blit(txt_rendering2, (1030,650))
                pass
            else:
                self.screen.blit(txt_rendering2, (1030,650))
                pass

    def sprawdz_walke(self,screen,walka_status):
        self.bandyta = random.randint(1, 5)
        if self.bandyta == 3:
            self.walka_status = True
            self.okno_walki(self.screen)
            pass

        else:
            pass
