import pygame
import sys
import pytmx
import mapa
import dialogy

import nastaveni as imgs

pygame.init()
pygame.font.init()


class Hra:

    def __init__(self, x=100, y=100, rychlost=4):
        self.rychlost = rychlost
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        self.running = True
        self.dialog = "None"
        self.font = pygame.font.Font("pokemon_pixel_font.ttf", 64)


        # --- MAPA --- #
        self.screen = pygame.display.set_mode((imgs.sirka_okna, imgs.vyska_okna))
        self.map = pytmx.load_pygame("map.tmx", pixelalpha=True)
        self.map_width = self.map.width * self.map.tilewidth
        self.map_height = self.map.height * self.map.tileheight
        self.postava = imgs.postava
        self.postava_height = self.postava.get_height()
        self.postava_width = self.postava.get_width()

    def hybani(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            if self.rychlost <= 8:
                self.rychlost = self.rychlost + 1
        else:
            self.rychlost = 4

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

    def loop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.dialog = dialogy.dialog1
                    elif event.key == pygame.K_r:
                        self.dialog = dialogy.dialog2

            self.hybani()

            self.x = max(0, min(self.x, self.map_width - self.postava_width))
            self.y = max(0, min(self.y, self.map_height - self.postava_height))
            self.camera_x = self.x - imgs.sirka_okna // 2
            self.camera_y = self.y - imgs.vyska_okna // 2
            self.camera_x = max(0, min(self.camera_x, self.map_width - imgs.sirka_okna))
            self.camera_y = max(0, min(self.camera_y, self.map_height - imgs.vyska_okna))

            mapa.draw_map(self.screen, self.map, self.camera_x, self.camera_y)
            self.text = self.font.render(self.dialog, False, (0, 0, 0))
            self.screen.blit(self.postava, (self.x - self.camera_x, self.y - self.camera_y))
            self.screen.blit(imgs.dialogoveokno,(200, 600))
            self.screen.blit(self.text, (250, 640))
            pygame.display.flip()
            self.clock.tick(60)


hra = Hra()
hra.loop()
