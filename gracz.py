import pygame
from pygame.math import Vector2
import random

class Player():

    def __init__(self):
        self.hp = 100
        self.gold = 0
        self.losowe_zdarzenia = random.randint(20, 35)
        print(self.losowe_zdarzenia)


    def random(self,black):
        font = pygame.font.SysFont("dejavusans", 20)
        self.los = random.randint(1, 6)
        text = str(self.los)
        text2 = "Twoja liczba to: "
        txt_rendering = font.render(text, 1, (250, 250, 250))
        txt_rendering2 = font.render(text2, 1, (250, 250, 250))
        zaslona = pygame.Rect(30, 550, 40, 40)
        zaslona_napis = pygame.Rect(60, 550, 165, 40)
        pygame.draw.rect(self.screen, self.black, zaslona)
        pygame.draw.rect(self.screen, self.black, zaslona_napis)
        self.screen.blit(txt_rendering2, (30, 550))
        self.screen.blit(txt_rendering, (190, 550))
        pygame.display.flip()

    def move(self,wspolrzedne_srodkow,green,ruch,black,screen):

        tempRuch = self.ruch + self.los
        if tempRuch >= len(self.wspolrzedne_srodkow):
            pionek = pygame.Rect(200, 410, 50, 50)
            pygame.draw.rect(self.screen, self.green, pionek)
            self.wspolrzedne_srodkow.append(Vector2((200,410)))
            self.ruch = tempRuch
            self.screen.fill(self.black)
            pass

        else:
            self.pole = self.wspolrzedne_srodkow[tempRuch]
            figura = pygame.Rect(self.pole.x, self.pole.y, 50, 50)
            pygame.draw.rect(self.screen, self.green, figura)
            self.ruch = tempRuch
        pygame.display.flip()


    def sprawdz_zdarzenia(self):
        for i in range(0,self.losowe_zdarzenia):
            if self.wspolrzedne_srodkow[i] == self.pole:
                print("znalazles skrzynie ze zlotem dostajesz 20 szt zlota!")
                self.gold += 20
                pass
            else:
                pass
