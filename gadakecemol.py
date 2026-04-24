import pygame
import sys
import pytmx

#testuju verified jen idkaaaa
# to je trochu random ale videl jsem ze se to takhle delaj aby to bylo prehlednejsi a pak to muzes vsechno zmenit na
# jednom miste
import nastaveni as imgs

pygame.init()




class Hra:

    def __init__(self, x = 100, y = 100 , rychlost = 1):
        self.rychlost = rychlost
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((imgs.sirka_okna, imgs.vyska_okna))
        self.mapa = imgs.mapa
        self.postava = imgs.postava

    def hybani(self):

        keys = pygame.key.get_pressed()



        if keys[pygame.K_w] and (keys[pygame.K_d] or keys[pygame.K_a]):
            self.y -= self.rychlost
        elif keys[pygame.K_w]:
            self.y -= self.rychlost
            self.postava = imgs.zadek
        if keys[pygame.K_s]:
            self.y += self.rychlost
            self.postava = imgs.postava
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.x -= self.rychlost
            self.postava = imgs.leva
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.x += self.rychlost
            self.postava = imgs.prava
    def postava(self, y, x):
        super().__init__(y, x)

    def loop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.hybani()
            self.screen.blit(self.mapa, (0, 0))
            self.screen.blit(self.postava, (self.x, self.y))
            pygame.display.flip()
            self.clock.tick(60)

            # pridal sem dalsi dimenzi haha chapes jako cas


hra = Hra()
hra.loop()
