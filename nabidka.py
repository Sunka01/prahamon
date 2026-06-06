import pygame
import sys
import save
import prahadex
import npc

def draw(screen, imgs, font):
    screen.blit(imgs.menu, (930, 30))
    inv = font.render("Inventar", False, (0, 0, 0))
    invb = font.render("Inventar", False, (140, 140, 140))
    screen.blit(invb, (1053, 78))
    screen.blit(inv, (1050, 75))
    mapab = font.render("Mapa", False, (140, 140, 140))
    screen.blit(mapab, (1053, 143))
    mapa = font.render("Mapa", False, (0, 0, 0))
    screen.blit(mapa, (1050, 140))
    prahadexb = font.render("PrahaDex", False, (140, 140, 140))
    screen.blit(prahadexb, (1053, 208))
    prahadex = font.render("PrahaDex", False, (0, 0, 0))
    screen.blit(prahadex, (1050, 205))
    hracb = font.render("Hrac", False, (140, 140, 140))
    screen.blit(hracb, (1053, 273))
    hrac = font.render("Hrac", False, (0, 0, 0))
    screen.blit(hrac, (1050, 270))
    quitb = font.render("Ukoncit", False, (140, 140, 140))
    screen.blit(quitb, (1053, 338))
    quit = font.render("Ukoncit", False, (0, 0, 0))
    screen.blit(quit, (1050, 335))


# sipecka

def sipecka(screen, imgs, pozicemenu):
    if pozicemenu == 1:
        screen.blit(imgs.sipka, (960, 70))
    elif pozicemenu == 2:
        screen.blit(imgs.sipka, (960, 135))
    elif pozicemenu == 3:
        screen.blit(imgs.sipka, (960, 200))
    elif pozicemenu == 4:
        screen.blit(imgs.sipka, (960, 265))
    elif pozicemenu == 5:
        screen.blit(imgs.sipka, (960, 330))


def handle(hra, event):
    if not hra.show_inventar or not hra.show_prahadex or not hra.show_mapa or not hra.shop:
        if event.key == pygame.K_w:
            if hra.pozicemenu > 1:
                hra.pozicemenu -= 1
        if event.key == pygame.K_s:
            if hra.pozicemenu < 5:
                hra.pozicemenu += 1

    if hra.pozicemenu == 5 and event.key == pygame.K_e:
        save.ulozit(hra)
        pygame.quit()
        sys.exit()
    elif hra.pozicemenu == 4 and event.key == pygame.K_e:
        pass
    elif hra.pozicemenu == 3 and event.key == pygame.K_e:
        hra.show_prahadex = True
        hra.menu = False
        hra.current_music = None
    elif hra.pozicemenu == 2 and event.key == pygame.K_e:
        hra.show_mapa = True
        hra.menu = False
        hra.current_music = None
    elif hra.pozicemenu == 1 and event.key == pygame.K_e:
        hra.show_inventar = True
        hra.menu = False
        hra.current_music = None

    if event.key == pygame.K_p:
        hra.penize += 100
        prahadex.prahadex.add(npc.Prahamon("Ptak", 10, 15, 1, [npc.Ability("Zobani", 5, 35, 35)]))
    if event.key == pygame.K_l:
        prahadex.prahadex.prahamoni["Ptak"].abilities.append(npc.Ability("Klovani", 10, 20, 20))
