import pygame
import sys
import pytmx
#to je trochu random ale videl jsem ze se to takhle delaj aby to bylo prehlednejsi a pak to muzes vsechno zmenit na jednom miste
from nastaveni import *

pygame.init()

class Hrac:
    def __init__(self, x, y, rychlost, keys):
        # tady proste to jakoze zarizuje tu lokaci a chuzi visco

        self.rychlost = rychlost
        self.x = x
        self.y = y


        #to by melo byt zvlast ne? ten __init__ se spusti jen jednou
    def hybani(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and (keys[pygame.K_d] or keys[pygame.K_a]):
            self.y -= self.rychlost
        elif keys[pygame.K_w]:
            self.y -= self.rychlost
        if keys[pygame.K_s]:
            self.y += self.rychlost
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.x -= self.rychlost

class Hra:
    def __init__(self):
        self.screen = pygame.display.set_mode((sirka_okna, vyska_okna))
        self.mapa = pygame.image.load("obrazky/mapa/img.png")
        self.clock = pygame.time.Clock()
        self.running = True


    def loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.mapa, (0, 0))

            pygame.display.flip()
            #pridal sem dalsi dimenzi haha chapes jako cas
            self.clock.tick(60)


hra = Hra()
hra.loop()
