import pygame
import prahadex
import npc

sirka_okna = 1280
vyska_okna = 800
rychlost_animace_chuze = 0.2


def img(path, size=None):
    image = pygame.image.load(path)
    if size:
        image = pygame.transform.scale(image, size)
    return image


velikost_postavy = (96, 96)

oak = img("obrazky/oak.png", (51,64))

doctor = img("obrazky/doctor.png", velikost_postavy)
cong = img("obrazky/cong.png", velikost_postavy)
babisek = img("obrazky/babisek.png", (92, 70))


postava = []
postava.append(img("obrazky/predek_1.png", velikost_postavy))
postava.append(img("obrazky/predek_2.png", velikost_postavy))
postava.append(img("obrazky/predek_3.png", velikost_postavy))
postava.append(img("obrazky/predek_4.png", velikost_postavy))

zadek = []
zadek.append(img("obrazky/zadek_1.png", velikost_postavy))
zadek.append(img("obrazky/zadek_2.png", velikost_postavy))
zadek.append(img("obrazky/zadek_3.png", velikost_postavy))
zadek.append(img("obrazky/zadek_4.png", velikost_postavy))

leva = []
leva.append(img("obrazky/leva_1.png", velikost_postavy))
leva.append(img("obrazky/leva_2.png", velikost_postavy))
leva.append(img("obrazky/leva_3.png", velikost_postavy))
leva.append(img("obrazky/leva_4.png", velikost_postavy))

prava = []
prava.append(img("obrazky/prava_1.png", velikost_postavy))
prava.append(img("obrazky/prava_2.png", velikost_postavy))
prava.append(img("obrazky/prava_3.png", velikost_postavy))
prava.append(img("obrazky/prava_4.png", velikost_postavy))


mapa = img("obrazky/mapa/img.png", velikost_postavy)
prahadex = img("obrazky/prahadex.png", (sirka_okna, vyska_okna))
prahadexdesc = img("obrazky/prahadexshow.png", (sirka_okna, vyska_okna))
inventar = img("obrazky/inventar.png", (sirka_okna, vyska_okna))
mapicka = img("obrazky/mapa/mapicka.png", (sirka_okna, vyska_okna))
dialogoveokno = img("obrazky/dialogoveokno.png", (sirka_okna, vyska_okna))
menu = img("obrazky/menu.png", (350, 400))
battlemenu = img("obrazky/battlemenu.png", (sirka_okna, vyska_okna))
battleground= img("obrazky/battleground.png", (sirka_okna, vyska_okna))
shop = img("obrazky/shop.png", (sirka_okna, vyska_okna))
heal = img("obrazky/heal.png", (sirka_okna, vyska_okna))


sipka = img("obrazky/sipka.png", (60, 60))
sipkainv = img("obrazky/sipkainv.png", (60, 60))
sipkaphd = img("obrazky/sipkaphd.png", (60, 60))
sipkashop = img("obrazky/sipkashop.png", (60, 60))
sipkabattle = img("obrazky/sipka.png", (30, 30))

# ---- PREDMETY -----

prahaball = img("obrazky/prahabally/prahaballbasic.png", (48, 48))
pivko = img("obrazky/prahabally/pivko.png", (24, 45))


# sem proste davej ty obrazky ono by se to pak moc stradalo, az toho bude vic rozdelime to do vic categories

# ---- PRAHAMONI -----

ptakzepredu = img("obrazky/prahamoni/ptakpredek.png", (440, 380))
ptak = img("obrazky/prahamoni/ptak.png", (480, 480))
twitter = img("obrazky/prahamoni/twitter.png", (480, 480))
twilight = img("obrazky/prahamoni/twilight.png", (480, 480))

prahamon_obrazky = {
    "Ptak;": ptakzepredu,
    "Ptak": ptak,
    "Twitter": twitter,
    "Twilight": twilight,
}
