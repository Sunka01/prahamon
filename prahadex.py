import pygame
import npc


class Prahadex:
    def __init__(self, capacity = 999):
        self.prahamoni = {}
        self.capacity = capacity

    def add(self, prahamon):
        self.prahamoni[prahamon.name] = prahamon
        return True

    def remove(self, item, amount=1):
        if self.prahamoni.get(item, 0) >= amount:
            self.prahamoni[item] -= amount
            if self.prahamoni[item] == 0:
                del self.prahamoni[item]
            return True
        return False

    def draw(self, screen, font, offset=0, limit=4):
        x, y = 830, 110
        items = list(self.prahamoni.values())  # ← .values() not .pm()
        visible = items[offset:offset + limit]
        for p in visible:
            text = font.render(f"{p.name} : {p.hp}hp", True, (0, 0, 0))
            screen.blit(text, (x, y))
            y += 120    


def sipecka(screen, imgs, pozice, offset=0):
    relative_pos = pozice - offset
    y = 100 + (relative_pos - 1) * 120
    screen.blit(imgs.sipkainv, (730, y))


prahadex = Prahadex()
