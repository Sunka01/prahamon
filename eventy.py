import pygame
import sys
import battle
import databaze
import inventar
import prahadex
import npc
import shop
import nastaveni as imgs
import save
import nabidka as menu_nabidka

#aaaa

def handle(hra, event):
    if event.type == pygame.QUIT:
        save.ulozit(hra)
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:

            if hra.med:
                if hra.medp == 1:
                    for p in prahadex.prahadex.prahamoni.values():
                        p.hp = p.maxhp
                    hra.med = False
                    hra.show = False
                    hra.zaplejdialog = False
                if hra.medp == 2:
                    hra.med = False
                    hra.show = False
                    hra.zaplejdialog = False
                    hra.medp = 1
            elif hra.show or hra.zaplejdialog and not hra.med:
                hra.zaplejdialog = False
                hra.show = False
            elif hra.kolize and hra.kolizenpc and not hra.show and not hra.shop and not hra.menu and not hra.show_inventar and not hra.show_prahadex and not hra.show_mapa:
                if hra.kolizenpc.name == "doctor":
                    hra.dialog = hra.kolizenpc.dialog
                    hra.show = True
                    hra.zaplejdialog = True
                    hra.med = True
                elif hra.kolizenpc.name == "cong":
                    if not hra.shop and not hra.menu and not hra.show_inventar and not hra.show_prahadex and not hra.show_mapa:
                        hra.shop = True
                        hra.shopopen = True
                elif hra.kolizenpc.dialog != "None":
                    hra.dialog = hra.kolizenpc.dialog
                    hra.show = True
                    hra.zaplejdialog = True
            if hra.show_prahadex:
                if hra.show_prahadexmenu:
                    if hra.pozicephdxmenu == 1:
                        hra.pozicephdxmenu = 1
                        hra.abilitymenu = True
                        hra.show_prahadexmenu = False
                    if hra.pozicephdxmenu == 2:
                        prahamoni = list(prahadex.prahadex.prahamoni.values())
                        if prahamoni and hra.poziceinventare <= len(prahamoni):
                            vybran = prahamoni[hra.poziceinventare - 1]
                            del prahadex.prahadex.prahamoni[vybran.name]
                            prvni = {vybran.name: vybran}
                            for stary, novy in prahadex.prahadex.prahamoni.items():
                                prvni[stary] = novy
                            prahadex.prahadex.prahamoni = prvni
                            hra.show_prahadexmenu = False
                            hra.poziceinventare = 1
                    if hra.pozicephdxmenu == 4:
                        hra.show_prahadexmenu = False
                elif hra.abilitymenu:
                    pass
                elif not hra.show_prahadexmenu:
                    hra.show_prahadexmenu = True


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
                        hra.nedostatek = True
            for item in hra.predmety:
                item.sebrano(hra.mchitboxcol, inventar.inventory)

        if not hra.shop and not hra.show and not hra.shopopen and not hra.show_prahadex and not hra.show_mapa and not hra.battle:
            if event.key == pygame.K_ESCAPE:
                hra.menu = not hra.menu
                hra.current_music = None


        if event.key == pygame.K_h:
            hra.oak_chce_jit = True



        if hra.menu:
            menu_nabidka.handle(hra, event)


        if hra.show_inventar:
            if event.key == pygame.K_ESCAPE:
                hra.show_inventar = False
                if not hra.battle:
                    hra.menu = True
                hra.poziceinventare = 1
                hra.inventar_offset = 0
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
            prahadex.handle(hra, event)

        if hra.show_mapa:
            if event.key == pygame.K_ESCAPE:
                hra.show_mapa = False
                hra.menu = True

        if hra.battle:
            battle.handle(hra, event)

        if hra.med:
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if hra.medp == 1:
                    hra.medp = 2
                elif hra.medp == 2:
                    hra.medp = 1

        if hra.shop:
            if event.key == pygame.K_w:
                if hra.poziceinventare > 1:
                    hra.poziceinventare -= 1
                    if hra.poziceinventare < hra.inventar_offset + 1:
                        hra.inventar_offset -= 1
            if event.key == pygame.K_s:
                if hra.poziceinventare < len(shop.shop.nabidka):
                    hra.poziceinventare += 1
                    if hra.poziceinventare > hra.inventar_offset + 4:
                        hra.inventar_offset += 1

        if event.key == pygame.K_ESCAPE:
            if hra.shop:
                hra.shop = False
                hra.menu = False
                hra.shopopen = False
                hra.poziceinventare = 1
                hra.inventar_offset = 0
                hra.current_music = None
