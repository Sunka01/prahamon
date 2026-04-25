import pygame

sirka_okna = 1280
vyska_okna = 800


def img(path, size=None):
    image = pygame.image.load(path)
    if size:
        image = pygame.transform.scale(image, size)
    return image


velikost_postavy = (51, 64)
postava = img("obrazky/predek.png", velikost_postavy)
zadek = img("obrazky/zadek.png", velikost_postavy)
leva = img("obrazky/leva.png", velikost_postavy)
prava = img("obrazky/prava.png", velikost_postavy)
mapa = img("obrazky/mapa/img.png", velikost_postavy)
dialogoveokno = img("obrazky/dialogoveokno.png", (880,150))

# sem proste davej ty obrazky ono by se to pak moc stradalo, az toho bude vic rozdelime to do vic categories
