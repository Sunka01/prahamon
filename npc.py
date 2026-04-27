import pygame
import random
import prahadex


class Npc:
    def __init__(self, name, image, x, y, dialog="nic"):
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

    def kolize(self, hrachitbox):
        return hrachitbox.colliderect(self.hitbox)

class Prahamon:
    def __init__(self, name, hp, image, x, y):
        self.name = name
        self.hp = hp
        self.image = image
        self.x = x
        self.y = y
        self.visible = True

    #def pridej_prahamon(self):


