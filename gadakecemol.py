import databaze, mapa, nabidka, eventy, inventar, npc, predmety, pygame, pytmx, battle, prahadex
import nastaveni as imgs
import shop
from npc import *
import random

pygame.init()
pygame.font.init()
pygame.display.set_caption("Prahamon")


class Hra:

    def __init__(self, x=310, y=360, rychlost=4, pozicemenu=1, poziceinventare=1, pozicephdxmenu=1):



        self.prahamoni = None
        self.rychlost = rychlost
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        self.running = True
        self.dialog = "None"
        self.font = pygame.font.Font("pokemon_pixel_font.ttf", 64)
        self.bigfont = pygame.font.Font("pokemon_pixel_font.ttf", 82)
        self.animace_chozeni_ted = 0
        self.posledni_smer = imgs.postava
        self.show = False
        self.zaplejdialog = False
        self.nejakejplaceholder = False


        self.kolize = False
        self.kolizenpc = None

        self.menu = False
        self.abilitymenu = False

        self.pozicemenu = pozicemenu
        self.pozice = pozicemenu
        self.poziceinventare = poziceinventare
        self.pozicephdxmenu = pozicephdxmenu

        self.show_inventar = False
        self.show_prahadex = False
        self.show_prahadexmenu = False
        self.show_mapa = False
        self.inventar_offset = 0

        self.oak_chce_jit = False

        self.nedostatek = False
        self.penize = 100
        self.shop = False
        self.shopopen = False

        self.catch = False
        self.battle = False
        self.med = False
        self.medp = 1

        self.current_music = None

        self.starapozicex = self.x
        self.starapozicey = self.y

        zobani = npc.Ability("Zobani", 5, 35, 35)
        klovani = npc.Ability("Klovani", 10, 20, 20)
        sykot = npc.Ability("Sykot", 15, 15, 15)


        self.predmety = [
            predmety.Predmet("Prahaball", imgs.prahaball, 1620, 1220),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 1220),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 1120),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 1020),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 920),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 820),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 720),
            # sem muzes davat predmety
        ]
        self.npc = [
            npc.Npc("oak", imgs.oak, 1620, 1420, dialog=databaze.dialog1),
            npc.Npc("babisek", imgs.babisek, 1660, 1420, dialog=databaze.dialog2),
            npc.Npc("cong", imgs.cong, 660, 420),
            npc.Npc("doctor", imgs.doctor, 1060, 1420, dialog="Chces vylecit sve Prahamony?")
        ]
            # sem muzes davat npcs


        self.prahamon = [
            npc.Prahamon("Ptak", 10, 15, 1, [zobani, klovani, sykot]),
            npc.Prahamon("Twitter", 15, 15, 2, [zobani, klovani]),
            npc.Prahamon("Twilight", 20, 20, 3, [zobani, sykot]),
            # prahamoni
        ]

        self.protivnici = [
            npc.Prahamon("Ptak;", 10, 15, 1, [zobani, sykot]),
            npc.Prahamon("Twitter", 15, 15, 2, [zobani, sykot]),
            npc.Prahamon("Twilight", 20, 20, 3, [zobani, sykot]),

        ]

        for p in self.prahamon:
            prahadex.prahadex.add(p)

        # --- MAPA --- #
        self.screen = pygame.display.set_mode((imgs.sirka_okna, imgs.vyska_okna))
        self.map = pytmx.load_pygame("map.tmx", pixelalpha=True)
        self.zdi = mapa.nacti_hitboxy_mapy(self.map)
        self.map_width = self.map.width * self.map.tilewidth
        self.map_height = self.map.height * self.map.tileheight

        self.postava = imgs.postava[0]
        self.postava_height = self.postava.get_height()
        self.postava_width = self.postava.get_width()

    def npc_movement(self):
        cil_y = 1620
        cil_x = 1200
        rychlost = 2
        self.npc[0].hitbox = pygame.Rect(cil_x, cil_y, self.npc[0].image.get_width(), self.npc[0].image.get_height())
        if self.npc[0].y < cil_y:
            self.npc[0].y += rychlost

        if self.npc[0].x > cil_x and self.npc[0].y == cil_y:
            self.npc[0].x -= rychlost
        if self.npc[0].x == cil_x and self.npc[0].y == cil_y:
            self.npc[0].visible = False
            self.npc[0].hitbox = pygame.Rect(-1, -2, -3, -4)



    def hybani(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            imgs.rychlost_animace_chuze = 0.4
            if self.rychlost <= 8:
                self.rychlost += 1
        else:
            self.rychlost = 4
            imgs.rychlost_animace_chuze = 0.2

        self.starapozicex = self.x
        self.starapozicey = self.y

        if not self.menu and not self.show and not self.show_mapa and not self.show_prahadex and not self.show_inventar and not self.shop and not self.battle and not self.med:

            if keys[pygame.K_w]:
                self.y -= self.rychlost
                self.posledni_smer = imgs.zadek
                self.postava = self.posledni_smer[int(self.animace_chozeni_ted)]
            elif keys[pygame.K_s]:
                self.y += self.rychlost
                self.posledni_smer = imgs.postava
                self.postava = self.posledni_smer[int(self.animace_chozeni_ted)]
            elif keys[pygame.K_a] and not keys[pygame.K_d]:
                self.x -= self.rychlost
                self.posledni_smer = imgs.leva
                self.postava = self.posledni_smer[int(self.animace_chozeni_ted)]
            elif keys[pygame.K_d] and not keys[pygame.K_a]:
                self.x += self.rychlost
                self.posledni_smer = imgs.prava
                self.postava = self.posledni_smer[int(self.animace_chozeni_ted)]
            else:
                self.animace_chozeni_ted = 0
                self.postava = self.posledni_smer[int(self.animace_chozeni_ted)]

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



    def loop(self):
        while self.running:
            for event in pygame.event.get():
                eventy.handle(self, event)
            self.hybani()
            self.camera()
            self.random = random.randint(1, 3)
            self.randomtrava = random.randint(1, 500)

            if self.current_music is None:
                pygame.mixer.init()
                pygame.mixer.music.load("muzika/menu.mp3")
                pygame.mixer.music.play(-1)
                self.current_music = "game"

            if hra.oak_chce_jit:
                hra.npc_movement()

            self.mchitbox = pygame.Rect(self.x + 5 - self.camera_x, self.y + 8 - self.camera_y, self.postava_width - 10,
                                        self.postava_height - 8)
            self.mchitboxcol = pygame.Rect(self.x + 10, self.y + 16, self.postava_width - 20, self.postava_height - 16)

            self.trava = pygame.Rect(1060 - self.camera_x, 0 - self.camera_y, 820, 400)

            mapa.vykresli_zem(self.screen, self.map, self.camera_x, self.camera_y)


            self.text = self.font.render(self.dialog, False, (0, 0, 0))
            self.textshadow = self.font.render(self.dialog, False, (150, 150, 150))

            self.kolize = False
            self.kolizenpc = None

            for item in self.npc:
                item.draw(self.screen, self.camera_x, self.camera_y)

            for item in self.predmety:
                item.draw(self.screen, self.camera_x, self.camera_y)

            self.screen.blit(self.postava, (self.x - self.camera_x, self.y - self.camera_y))

            """HITBOXY"""
            #for id in self.npc: pygame.draw.rect(self.screen, (255, 0, 255), (id.hitbox.x - self.camera_x,id.hitbox.y - self.camera_y,id.hitbox.width,id.hitbox.height), 4)

            """MAIN CHARACTER"""
            pygame.draw.rect(self.screen, (255, 0, 0), self.mchitbox, 2)
            """ZDI"""
            for zed in self.zdi:
                pass
                #pygame.draw.rect(self.screen, (255, 0, 0),(zed.x - self.camera_x, zed.y - self.camera_y, zed.width, zed.height), 4)
            for zed in self.zdi:
                if self.mchitboxcol.colliderect(zed):
                    self.x = self.starapozicex
                    self.y = self.starapozicey
                    # TODO: TADY NEJAK CHECKNOUT A ZASTAVIT CHUZI ALE ABY NEBYLA ZASTAVENAAA


            for item in self.npc:
                if item.kolize(self.mchitboxcol):
                    self.kolize = True
                    self.kolizenpc = item
                    break

            if hra.battle:
                battle.draw(self.screen, self.font, self)
                battle.sipecka(self.screen, imgs, self.pozice)

            if self.randomtrava == 20 and self.mchitbox.colliderect(self.trava) and not hra.battle and not hra.menu:
                hra.protivnici[0].hp = hra.protivnici[0].maxhp
                self.battle = True

            if self.menu:
                if self.current_music != "menu":
                    pygame.mixer.music.load("muzika/surprises.mp3")
                    pygame.mixer.music.play(-1)
                    self.current_music = "menu"
                nabidka.draw(self.screen, imgs, self.font)
                nabidka.sipecka(self.screen, imgs, self.pozicemenu)

            if self.show_inventar:
                self.screen.blit(imgs.inventar, (0, 0))
                self.screen.blit(self.bigfont.render("INVENTAR", False, (50, 50, 50)), (125, 95))
                self.screen.blit(self.bigfont.render("INVENTAR", False, (255, 255, 255)), (120, 90))
                inventar.inventory.draw(self.screen, self.font, self.inventar_offset, 4)
                inventar.sipecka(self.screen, imgs, self.poziceinventare, self.inventar_offset)

            if self.show_prahadex:
                self.screen.blit(imgs.prahadex, (0, 0))
                self.screen.blit(imgs.prahadexdesc, (0, 0))
                self.screen.blit(self.bigfont.render("PRAHADEX", False, (50, 50, 50)), (125, 95))
                self.screen.blit(self.bigfont.render("PRAHADEX", False, (255, 255, 255)), (120, 90))
                prahadex.prahadex.draw(self.screen, self.font, self.inventar_offset, 4, self.poziceinventare, imgs,
                                       self.show_prahadexmenu, self.abilitymenu)
                prahadex.sipecka(self.screen, imgs, self.poziceinventare, self.pozicephdxmenu, self.show_prahadexmenu,
                                 self.inventar_offset, self.abilitymenu)

            if self.show_mapa:
                self.screen.blit(imgs.mapicka, (0, 0))
                self.screen.blit(self.font.render("PRAHA", False, (0, 0, 0)), (250, 120))

            if self.shop:
                self.screen.blit(imgs.shop, (0, 0))
                self.screen.blit(self.bigfont.render("U PANA DONGA", False, (50, 50, 50)), (125, 95))
                self.screen.blit(self.bigfont.render("U PANA DONGA", False, (255, 255, 255)), (120, 90))
                self.screen.blit(self.font.render(f"{self.penize}Czk", False, (50, 50, 50)), (303, 253))
                self.screen.blit(self.font.render(f"{self.penize}Czk", False, (255, 255, 255)), (300, 250))
                shop.shop.draw(self.screen, self.font, self.inventar_offset, 4)
                shop.sipecka(self.screen, imgs, self.poziceinventare, self.inventar_offset)



            if hra.catch and hra.nejakejplaceholder:
                if inventar.inventory.has("prahaball"):
                    if self.random == 3:
                        inventar.inventory.remove("prahaball")
                        self.prahamon.append(npc.Prahamon("Ptak",15))
                        prahadex.prahadex.add(self.prahamon[-1])
                        self.npc[1].visible = False
                        self.dialog = "Chytl jsi ho! "
                    else:
                        inventar.inventory.remove("prahaball")
                        self.dialog = "Nechytl jsi ho!"
                    self.show = True
                    self.catch = False
                elif not inventar.inventory.has("prahaball"):
                    self.dialog = "Zadny prahaball!"
                    self.show = True
                    self.catch = False


            # pygame.draw.rect(self.screen, (0, 0, 0), (1060 - self.camera_x, 0 - self.camera_y, 820, 400), 2)


            if self.show or self.zaplejdialog:
                self.screen.blit(imgs.dialogoveokno, (0,0))
                self.screen.blit(self.textshadow, (183, 643))
                self.screen.blit(self.text, (180,640))
                if self.med:
                    self.screen.blit(imgs.heal, (0,0))
                    self.screen.blit(self.font.render("Ano", False, (150, 150, 150)), (1123, 613))
                    self.screen.blit(self.font.render("Ano", False, (0, 0, 0)), (1120, 610))
                    self.screen.blit(self.font.render("Ne", False, (150, 150, 150)), (1123, 668))
                    self.screen.blit(self.font.render("Ne", False, (0, 0, 0)), (1120, 665))
                    if self.medp == 1:
                        self.screen.blit(imgs.sipkaphd, (1060,610))
                    elif self.medp == 2:
                        self.screen.blit(imgs.sipkaphd, (1060,665))

            if self.nedostatek:
                npa = self.bigfont.render("Nedostatek penez ", False, (150, 150, 150))
                np = self.bigfont.render("Nedostatek penez ", False, (255, 255, 255))
                self.screen.blit(npa, (653, 563))
                self.screen.blit(np, (650, 560))
                pygame.display.update()
                pygame.time.delay(700)

                self.nedostatek = False

            self.animace()
            pygame.display.flip()
            self.clock.tick(60)


hra = Hra()
hra.loop()
