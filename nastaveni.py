import pygame

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
ptak = img("obrazky/ptak.png", (51, 64))

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
inventar = img("obrazky/inventar.png", (sirka_okna, vyska_okna))
dialogoveokno = img("obrazky/dialogoveokno.png", (880,150))
menu = img("obrazky/menu.png", (350, 400))
sipka = img("obrazky/sipka.png", (60, 60))
sipkainv = img("obrazky/sipkainv.png", (60, 60))

# ---- PREDMETY -----

prahaball = img("obrazky/prahabally/prahaballbasic.png", (48, 48))
pivko = img("obrazky/prahabally/pivko.png", (24, 45))


# sem proste davej ty obrazky ono by se to pak moc stradalo, az toho bude vic rozdelime to do vic categories
