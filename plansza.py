import pygame, sys, random

class plansza(object):

    def __init__(self):
        """Konfiguracja, pętla główna, tytuł."""
        self.screen =  pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Plansza gry")
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


            #self.screen.fill((0, 0, 0))

    def rysuj(self):
        """Funkcja rysująca planszę."""
        self.kwadrat = pygame.Rect(self.size[0] / 2, self.size[1] / 2, 40, 40)
        self.kwadrat2 = pygame.Rect(self.size[0] / 2, self.size[1] / 2 - 41, 40, 40)
        self.kwadrat3 = pygame.Rect(self.size[0] / 2, self.size[1] / 2 - 82, 40, 40)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat2)
        pygame.draw.rect(self.screen, (0, 150, 255), self.kwadrat3)
        pygame.display.flip()

    def losowanie(self):
        """Funkcja losująca liczbę od 1 do 6 i wyświetlająca ją na ekranie."""
        self.oczko = random.randint(1, 6)
        self.czcionka = pygame.font.SysFont("dejavusans", 20)
        self.komunikat = str(self.oczko)
        self.renderowanie_tekstu = self.czcionka.render(self.komunikat, 1, (250, 250, 250))
        self.zaslona = pygame.Rect(10, 10, 40, 40)
        pygame.draw.rect(self.screen, (0, 0, 0), self.zaslona)
        self.screen.blit(self.renderowanie_tekstu, (10, 10))
        pygame.display.update()


if __name__ == '__main__':
    plansza()

