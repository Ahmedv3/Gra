import pygame, sys

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    size = screen.get_size()
    kwadrat = pygame.Rect(size[0]/2, size[1]/2, 40, 40)
    kwadrat2 = pygame.Rect(size[0]/2, size[1]/2-41, 40, 40)
    kwadrat3 = pygame.Rect(size[0]/2, size[1]/2-82, 40, 40)
    pygame.draw.rect(screen, (0, 150, 255), kwadrat)
    pygame.draw.rect(screen, (0, 150, 255), kwadrat2)
    pygame.draw.rect(screen, (0, 150, 255), kwadrat3)
    pygame.display.flip()