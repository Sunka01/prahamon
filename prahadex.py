import pygame
import npc
import nastaveni as imgs


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

    def draw(self, screen, font, offset=0, limit=4, pozice=1, imgs=None, menu = False):
        x, y = 830, 110
        items = list(self.prahamoni.values())
        visible = items[offset:offset + limit]
        if imgs is not None and items:
            vybran = items[pozice - 1] if pozice <= len(items) else items[0]

            obrazek = pygame.transform.scale(imgs.prahamon_obrazky.get(vybran.name), (250, 250))
            if obrazek:
                screen.blit(obrazek, (70, 260))
            screen.blit(font.render(f"{vybran.hp}/{vybran.maxhp}hp", True, (50, 50, 50)), (404, 281))
            screen.blit(font.render(f"{vybran.hp}/{vybran.maxhp}hp", True, (255, 255, 255)), (400, 277))
            screen.blit(font.render(f"{vybran.lvl}. lvl", True, (50, 50, 50)), (404, 351))
            screen.blit(font.render(f"{vybran.lvl}. lvl", True, (255, 255, 255)), (400, 347))
            screen.blit(font.render(f"{vybran.name}", True, (50, 50, 50)), (94, 579))
            screen.blit(font.render(f"{vybran.name}", True, (255, 255, 255)), (90, 574))

        if menu:
            screen.blit(font.render(f"Abilitky", True, (50, 50, 50)), (x + 4, y + 4))
            screen.blit(font.render(f"Abilitky", True, (255, 255, 255)), (x, y))
            screen.blit(font.render(f"Switch", True, (50, 50, 50)), (x + 4, y + 124))
            screen.blit(font.render(f"Switch", True, (255, 255, 255)), (x, y + 120))
            screen.blit(font.render(f"Exit", True, (50, 50, 50)), (x + 4, y + 364))
            screen.blit(font.render(f"Exit", True, (255, 255, 255)), (x, y + 360))
        elif not menu:
            for p in visible:
                screen.blit(font.render(f"{p.name}", True, (50, 50, 50)), (x + 4, y + 4))
                screen.blit(font.render(f"{p.name}", True, (255, 255, 255)), (x, y))

                y += 120


def sipecka(screen, imgs, pozice, pozicemenu, menu, offset=0):
    if not menu:
        relative_pos = pozice - offset
        y = 100 + (relative_pos - 1) * 120
        screen.blit(imgs.sipkaphd, (730, y))
    if menu:
        y = 100 + (pozicemenu - 1) * 120
        screen.blit(imgs.sipkaphd, (730, y))

prahadex = Prahadex()