import pygame
import pytmx
import mapa
import nabidka
import eventy
import inventar

import nastaveni as imgs

pygame.init()
pygame.font.init()
pygame.display.set_caption("Prahamon")


class Hra:

    def __init__(self, x=310, y=360, rychlost=4, pozicemenu=1):
        self.rychlost = rychlost
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        self.running = True
        self.dialog = "None"
        self.font = pygame.font.Font("pokemon_pixel_font.ttf", 64)
        self.animace_chozeni_ted = 0
        self.show = False
        self.kolize = False
        self.menu = False
        self.pozicemenu = pozicemenu

        # --- MAPA --- #
        self.screen = pygame.display.set_mode((imgs.sirka_okna, imgs.vyska_okna))
        self.map = pytmx.load_pygame("map.tmx", pixelalpha=True)
        self.zdi = mapa.nacti_hitboxy_mapy(self.map)
        self.map_width = self.map.width * self.map.tilewidth
        self.map_height = self.map.height * self.map.tileheight

        self.postava = imgs.postava[0]
        self.postava_height = self.postava.get_height()
        self.postava_width = self.postava.get_width()

    def hybani(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            imgs.rychlost_animace_chuze = 0.4
            if self.rychlost <= 8:
                self.rychlost += 1
        else:
            self.rychlost = 4
            imgs.rychlost_animace_chuze = 0.2

        if not self.menu and not self.show:

            if keys[pygame.K_w] and (keys[pygame.K_d] or keys[pygame.K_a]):
                self.y -= self.rychlost
            elif keys[pygame.K_w]:
                self.y -= self.rychlost
                self.postava = imgs.zadek[int(self.animace_chozeni_ted)]
            if keys[pygame.K_s]:
                self.y += self.rychlost
                self.postava = imgs.postava[int(self.animace_chozeni_ted)]
            if keys[pygame.K_a] and not keys[pygame.K_d]:
                self.x -= self.rychlost
                self.postava = imgs.leva[int(self.animace_chozeni_ted)]
            elif keys[pygame.K_d] and not keys[pygame.K_a]:
                self.x += self.rychlost
                self.postava = imgs.prava[int(self.animace_chozeni_ted)]




    def animace(self):
        keys = pygame.key.get_pressed()
        hybe_se = keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_a]

        if hybe_se:
            self.animace_chozeni_ted += imgs.rychlost_animace_chuze

            if self.animace_chozeni_ted >= 4:
                self.animace_chozeni_ted = 0
        else:
            self.animace_chozeni_ted = 0
    def camera(self):
        self.x = max(0, min(self.x, self.map_width - self.postava_width))
        self.y = max(0, min(self.y, self.map_height - self.postava_height))
        self.camera_x = self.x - imgs.sirka_okna // 2
        self.camera_y = self.y - imgs.vyska_okna // 2
        self.camera_x = max(0, min(self.camera_x, self.map_width - imgs.sirka_okna))
        self.camera_y = max(0, min(self.camera_y, self.map_height - imgs.vyska_okna))


        # TODO: Okay musime nejak vymyslet system inventare a prahadexu protoze to je takovy dost ze jsem unsure ale
        # TODO: possibly to nebude tak tezky, nevim do kdy budu spat takze klidne muzes neco zkusit

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                eventy.handle(self, event)
            self.hybani()
            self.camera()

            mchitbox = pygame.Rect(self.x + 5 - self.camera_x, self.y + 8 - self.camera_y, self.postava_width - 10, self.postava_height - 8)
            oakhitbox = pygame.Rect(1620, 1420, imgs.oak.get_width(), imgs.oak.get_height())
            mchitboxcol = pygame.Rect(self.x + 10, self.y + 16, self.postava_width - 20, self.postava_height - 16)

            mapa.vykresli_zem(self.screen, self.map, self.camera_x, self.camera_y)

            self.text = self.font.render(self.dialog, False, (0, 0, 0))

            self.screen.blit(imgs.oak, (1620 - self.camera_x, 1420 - self.camera_y))

            self.screen.blit(self.postava, (self.x - self.camera_x, self.y - self.camera_y))

            mapa.vykresli_vrchy_stromu(self.screen, self.map, self.camera_x, self.camera_y)

            pygame.draw.rect(self.screen, (255, 0, 0), mchitbox, 2)
            pygame.draw.rect(self.screen, (255, 255, 0), (oakhitbox.x - self.camera_x, oakhitbox.y - self.camera_y, oakhitbox.width, oakhitbox.height), 2)

            for zed in self.zdi:
                pass
                # pygame.draw.rect(self.screen, (255, 0, 0),(zed.x - self.camera_x, zed.y - self.camera_y, zed.width, zed.height), 4)


            if mchitboxcol.colliderect(oakhitbox):
                self.kolize = True
            else:
                self.kolize = False

            if self.kolize and self.show:
                self.screen.blit(imgs.dialogoveokno, (200, 600))
                self.screen.blit(self.text, (250, 640))

            if self.menu:
                nabidka.draw(self.screen, imgs, self.font)
                nabidka.sipecka(self.screen, imgs, self.pozicemenu)

            if self.menu and self.pozicemenu == 1:
                import inventar
                inventar.inventory.draw(self.screen, self.font)



            self.animace()
            pygame.display.flip()
            self.clock.tick(60)


hra = Hra()
hra.loop()
