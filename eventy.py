import pygame
import sys
import dialogy
import inventar
import prahadex


def handle(hra, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            if hra.show:
                hra.show = False
            elif hra.kolize and hra.kolizenpc:
                hra.dialog = hra.kolizenpc.dialog
                hra.show = True
            for item in hra.predmety:
                item.sebrano(hra.mchitboxcol, inventar.inventory)

        if event.key == pygame.K_ESCAPE:
            hra.menu = not hra.menu

        if hra.menu:
            if not hra.show_inventar or not hra.show_prahadex:
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
                hra.show_prahadex = True
            elif hra.pozicemenu == 2 and event.key == pygame.K_e:
                pass  # TODO: Mapa
            elif hra.pozicemenu == 1 and event.key == pygame.K_e:
                hra.show_inventar = True

        if hra.show_inventar:
            if event.key == pygame.K_ESCAPE:
                hra.show_inventar = False
            if event.key == pygame.K_w:
                if hra.poziceinventare > 1:
                    hra.poziceinventare -= 1
                    if hra.poziceinventare < hra.inventar_offset + 1:
                        hra.inventar_offset -= 1
            if event.key == pygame.K_s:
                if hra.poziceinventare < len(inventar.inventory.items):
                    hra.poziceinventare += 1
                    if hra.poziceinventare > hra.inventar_offset + 4:
                        hra.inventar_offset += 1

        if hra.show_prahadex:
            if event.key == pygame.K_ESCAPE:
                hra.show_prahadex = False
            if event.key == pygame.K_w:
                if hra.poziceinventare > 1:
                    hra.poziceinventare -= 1
                    if hra.poziceinventare < hra.inventar_offset + 1:
                        hra.inventar_offset -= 1
            if event.key == pygame.K_s:
                if hra.poziceinventare < len(prahadex.prahadex.items):
                    hra.poziceinventare += 1
                    if hra.poziceinventare > hra.inventar_offset + 4:
                        hra.inventar_offset += 1
