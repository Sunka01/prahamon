import pygame
import sys
import dialogy
import inventar

def handle(hra, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            if hra.kolize:
                hra.dialog = dialogy.dialog1
                hra.show = not hra.show
            if hra.prahaball and hra.mchitboxcol.colliderect(hra.ballhitbox):
                hra.prahaball = False
                inventar.inventory.add("prahaball")


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
            elif hra.pozicemenu == 4 and event.key == pygame.K_e:
                pass  # TODO: Mapa
            elif hra.pozicemenu == 3 and event.key == pygame.K_e:
                pass  # TODO: Mapa
            elif hra.pozicemenu == 2 and event.key == pygame.K_e:
                pass # TODO: Mapa
            elif hra.pozicemenu == 1 and event.key == pygame.K_e:
                pass  # TODO: Mapa
