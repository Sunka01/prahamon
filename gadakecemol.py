import pygame
import sys
import pytmx
# to je trochu random ale videl jsem ze se to takhle delaj aby to bylo prehlednejsi a pak to muzes vsechno zmenit na
# jednom miste
import nastaveni as imgs

pygame.init()


class Hrac:
    def __init__(self, x, y, rychlost):
        # tady proste to jakoze zarizuje tu lokaci a chuzi visco

        self.rychlost = rychlost
        self.x = x
        self.y = y

        # to by melo byt zvlast ne? ten __init__ se spusti jen jednou
        # mladej telinger nas to ucil takhle ale ja nevim ja moc nepouzival metody obecne

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
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((imgs.sirka_okna, imgs.vyska_okna))
        self.mapa = imgs.mapa

    def loop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.mapa, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

            # pridal sem dalsi dimenzi haha chapes jako cas


hra = Hra()
hra.loop()
