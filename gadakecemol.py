import pygame
import sys

pygame.init()


class Hrac:
    def __init__(self, x, y, rychlost, keys):
        keys = pygame.key.get_pressed()

        # tady proste to jakoze zarizuje tu lokaci a chuzi visco

        self.rychlost = rychlost
        self.x = x
        self.y = y

        if keys[pygame.K_w] and (keys[pygame.K_d] or keys[pygame.K_a]):
            y -= rychlost
        elif keys[pygame.K_w]:
            y -= rychlost
        if keys[pygame.K_s]:
            y += rychlost
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            x -= rychlost
        pygame.display.flip()


class Hra:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.mapa = pygame.image.load("obrazky/mapa/img.png")
        self.running = True

        pygame.display.flip()

    def loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.mapa, (0, 0))

            pygame.display.flip()


hra = Hra()
hra.loop()
