import pygame


class Inventory:
    def __init__(self, capacity=8):
        self.items = {}
        self.capacity = capacity

    def add(self, item, amount=1):
        if len(self.items) >= self.capacity:
            print("Plny inventar")
            return False
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

    def draw(self, screen, font):
        x, y = 830, 110
        for item, qty in self.items.items():
            text = font.render(f"{qty}x    {item} ", True, (0, 0, 0))
            screen.blit(text, (x, y))
            y += 120


inventory = Inventory(capacity=8)
