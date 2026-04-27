import pygame


class Prahadex:
    def __init__(self, hp,capacity=999):
        self.items = {}
        self.hp = hp
        self.ability = []
        self.capacity = capacity

    def add(self, item, hp, amount=1):
        self.hp = hp
        self.items[item] = self.items.get(item, 0) + amount
        return True

    def remove(self, item, amount=1):
        if self.items.get(item, 0) >= amount:
            self.items[item] -= amount
            if self.items[item] == 0:
                del self.items[item]
            return True
        return False

    def has(self, item, amount=1):
        return self.items.get(item, 0) >= amount

    def draw(self, screen, font, offset=0, limit=4):
        x, y = 830, 110
        items = list(self.items.items())
        visible = items[offset:offset + limit]
        for item, qty in visible:
            text = font.render(f"{item} : {self.hp}hp", True, (0, 0, 0))
            screen.blit(text, (x, y))
            y += 120


def sipecka(screen, imgs, pozice, offset=0):
    relative_pos = pozice - offset
    y = 100 + (relative_pos - 1) * 120
    screen.blit(imgs.sipkainv, (730, y))


prahadex = Prahadex(capacity=999,hp = 100)
