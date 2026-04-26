import pygame


class Predmet:
    def __init__(self, name, image, x, y):
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.visible = True
        self.hitbox = pygame.Rect(x, y, image.get_width(), image.get_height())

    def draw(self, screen, camera_x, camera_y):

        if self.visible:
            screen.blit(self.image, (self.x - camera_x, self.y - camera_y))
        pass
    def sebrano(self, player_rect, inventory):
        if self.visible and player_rect.colliderect(self.hitbox):
            self.visible = False
            inventory.add(self.name)
            return True
        return False
