import pygame
import random
import prahadex


class Npc:
    def __init__(self, name, image, x, y, dialog="None"):
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.dialog = dialog
        self.visible = True
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())

    def draw(self, screen, camera_x, camera_y):
        if self.visible:
            screen.blit(self.image, (self.x - camera_x, self.y - camera_y))
        else:
            self.hitbox = pygame.Rect(-1, -2, -3, -4)

    def kolize(self, hrachitbox):
        return hrachitbox.colliderect(self.hitbox)


class Ability:
    def __init__(self, name, damage, pp, max_pp):
        self.name = name
        self.damage = damage
        self.pp = pp
        self.max_pp = max_pp


class Prahamon:
    def __init__(self, name, hp, maxhp, lvl, abilities):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.lvl = lvl
        self.abilities = abilities if abilities is not None else []
