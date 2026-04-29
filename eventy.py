import pygame
import sys
import databaze
import inventar
import prahadex
import npc
import shop


def handle(hra, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            if hra.show or hra.zaplejdialog:
                hra.zaplejdialog = False
                hra.show = False
            elif hra.kolize and hra.kolizenpc and not hra.show:
                if hra.kolizenpc.dialog != "None":
                    hra.dialog = hra.kolizenpc.dialog
                    hra.show = True
                    hra.zaplejdialog = True
                elif hra.kolizenpc.name == "cong":
                    if not hra.shop and not hra.menu and not hra.show_inventar and not hra.show_prahadex and not hra.show_mapa:
                        hra.shop = True
                        hra.shopopen = True
                elif hra.kolizenpc.name == "ptak":
                    if not hra.catch and not hra.show:
                        hra.catch = True
                        hra.nejakejplaceholder = True

            if hra.shop and hra.shopopen:
                hra.shopopen = False
            elif hra.shop and not hra.show:
                nabidka = list(shop.shop.nabidka.values())
                if nabidka:
                    vyber = nabidka[hra.poziceinventare - 1]

                    if hra.penize >= vyber.cena:
                        inventar.inventory.add(vyber.name)
                        hra.penize -= vyber.cena
                    else:
                        hra.dialog = "Nedostatek penez"
                        hra.show = True
            if hra.show:
                hra.show = False
            for item in hra.predmety:
                item.sebrano(hra.mchitboxcol, inventar.inventory)

        if not hra.shop and not hra.show and not hra.shopopen and not hra.show_prahadex and not hra.show_mapa:
            if event.key == pygame.K_ESCAPE:
                hra.menu = not hra.menu


        if event.key == pygame.K_h:
            hra.oak_chce_jit = True

        if hra.menu:
            if not hra.show_inventar or not hra.show_prahadex or not hra.show_mapa or not hra.shop:
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
                hra.menu = False
            elif hra.pozicemenu == 2 and event.key == pygame.K_e:
                hra.show_mapa = True
                hra.menu = False
            elif hra.pozicemenu == 1 and event.key == pygame.K_e:
                hra.show_inventar = True
                hra.menu = False

        if hra.show_inventar:
            if event.key == pygame.K_ESCAPE:
                hra.show_inventar = False
                hra.menu = True
                hra.poziceinventare = 1
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
                hra.menu = True
                hra.poziceinventare = 1
            if event.key == pygame.K_w:
                if hra.poziceinventare > 1:
                    hra.poziceinventare -= 1
                    if hra.poziceinventare < hra.inventar_offset + 1:
                        hra.inventar_offset -= 1
            if event.key == pygame.K_s:
                if hra.poziceinventare < len(prahadex.prahadex.prahamoni):
                    hra.poziceinventare += 1
                    if hra.poziceinventare > hra.inventar_offset + 4:
                        hra.inventar_offset += 1

        if hra.show_mapa:
            if event.key == pygame.K_ESCAPE:
                hra.show_mapa = False
                hra.menu = True

        if event.key == pygame.K_ESCAPE:
            if hra.shop:
                hra.shop = False
                hra.menu = False
                hra.shopopen = False
                hra.poziceinventare = 1
