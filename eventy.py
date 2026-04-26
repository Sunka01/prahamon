import pygame
import sys
import dialogy

def handle(hra, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            hra.dialog = dialogy.dialog1
            hra.show = not hra.show

        if event.key == pygame.K_ESCAPE:
            hra.menu = not hra.menu

        if hra.menu:
            if event.key == pygame.K_w:
                if hra.pozicemenu > 1:
                    hra.pozicemenu -= 1
            if event.key == pygame.K_s:
                if hra.pozicemenu < 5:
                    hra.pozicemenu += 1
            if hra.pozicemenu == 5 and event.key == pygame.K_e:
                pygame.quit()
                sys.exit()