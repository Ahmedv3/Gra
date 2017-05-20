import pygame, sys, random

class plansza(object):

    def __init__(self):
        # Konfiguracja
        self.screen =  pygame.display.set_mode((800, 600))
        self.size = self.screen.get_size()
        pygame.init()
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit(0)
                elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_l:
                    self.losowanie()
                    print("Wyrzuciłeś:", self.oczko, "oczek.")
            self.rysuj()
            self.screen.fill((0, 0, 0))

    def rysuj(self):

        self.kwadrat = pygame.Rect(self.size[0] / 2, self.size[1] / 2, 40, 40)
        self.kwadrat2 = pygame.Rect(self.size[0] / 2, self.size[1] / 2 - 41, 40, 40)
        self.kwadrat3 = pygame.Rect(self.size[0] / 2, self.size[1] / 2 - 82, 40, 40)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat2)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat3)
        pygame.display.flip()

    def losowanie(self):
        self.oczko = random.randint(1, 6)

plansza()

