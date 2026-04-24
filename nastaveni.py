import pygame

sirka_okna = 831
vyska_okna = 800


def img(path, size=None):
    image = pygame.image.load(path)
    if size:
        image = pygame.transform.scale(image, size)
    return image


postava = ("obrazky/predek.png", (266, 313))
mapa = img("obrazky/mapa/img.png", (831, 800))

# sem proste davej ty obrazky ono by se to pak moc stradalo, az toho bude vic rozdelime to do vic categories
