import pygame
import npc


class Shop:
    def __init__(self, capacity=999):
        self.nabidka = {}
        self.capacity = capacity

    def add(self, vec):
        self.nabidka[vec.name] = vec
        return True

    def remove(self, vec, amount=1):
        if self.nabidka.get(vec, 0) >= amount:
            self.nabidka[vec] -= amount
            if self.nabidka[vec] == 0:
                del self.nabidka[vec]
            return True
        return False

    def draw(self, screen, font, offset=0, limit=4):
        x, y = 830, 110
        items = list(self.nabidka.values())
        visible = items[offset:offset + limit]
        for p in visible:
            text = font.render(f"{p.name} : {p.cena}Czk", True, (0, 0, 0))
            screen.blit(text, (x, y))
            y += 120


def sipecka(screen, imgs, pozice, offset=0):
    relative_pos = pozice - offset
    y = 100 + (relative_pos - 1) * 120
    screen.blit(imgs.sipkashop, (730, y))


class ShopList:
    def __init__(self, name, cena):
        self.name = name
        self.cena = cena


shop = Shop()

nab = [
    ShopList("prahaball", 100)
]

for p in nab:
    shop.add(p)
