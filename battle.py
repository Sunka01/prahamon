import pygame


import prahadex
import nastaveni as imgs



def draw(screen, font, hra):
    prahamon = list(prahadex.prahadex.prahamoni.values())[0]
    if not hra.protivnici:
        return
    protivnik = hra.protivnici[hra.protivnik_index]

    screen.fill((0, 40, 0))
    screen.blit(imgs.battleground, (0, 0))

    obrazek = imgs.prahamon_obrazky.get(prahamon.name)
    if obrazek:
        screen.blit(obrazek, (100, 220))

    imgprotivnika = imgs.prahamon_obrazky.get(protivnik.name)
    if imgprotivnika:
        screen.blit(imgprotivnika, (622, 33))

    screen.blit(imgs.battlemenu, (0, 0))
    screen.blit(font.render(f"{prahamon.name};", False, (150, 150, 150)), (922, 372))
    screen.blit(font.render(f"{prahamon.name};", False, (0, 0, 0)), (920, 370))

    screen.blit(font.render(f"lvl. {prahamon.lvl}", False, (150, 150, 150)), (1122, 372))
    screen.blit(font.render(f"lvl. {prahamon.lvl}", False, (0, 0, 0)), (1120, 370))

    screen.blit(font.render(f"HP: {prahamon.hp}/{prahamon.maxhp}", False, (150, 150, 150)), (922, 432))
    screen.blit(font.render(f"HP: {prahamon.hp}/{prahamon.maxhp}", False, (0, 0, 0)), (920, 430))

    screen.blit(font.render(f"{protivnik.name}", False, (150, 150, 150)), (78, 74))
    screen.blit(font.render(f"{protivnik.name}", False, (0, 0, 0)), (76, 72))

    screen.blit(font.render(f"lvl. {protivnik.lvl}", False, (150, 150, 150)), (282, 74))
    screen.blit(font.render(f"lvl. {protivnik.lvl}", False, (0, 0, 0)), (280, 72))

    screen.blit(font.render(f"HP: {protivnik.hp}/{protivnik.maxhp}", False, (150, 150, 150)), (78, 129))
    screen.blit(font.render(f"HP: {protivnik.hp}/{protivnik.maxhp}", False, (0, 0, 0)), (76, 127))

    if hra.abilitybattle:
        abilities = prahamon.abilities
        prvni = f"{abilities[0].name}" if len(abilities) > 0 else " "
        druhy = f"{abilities[1].name}" if len(abilities) > 1 else " "
        treti = f"{abilities[2].name}" if len(abilities) > 2 else " "
        ctvrty = f"{abilities[3].name}" if len(abilities) > 3 else " "
    elif not hra.abilitybattle:
        prvni = "Utok"
        druhy = "PD"
        treti = "Inventar"
        ctvrty = "Run"

    screen.blit(font.render(prvni, False, (150, 150, 150)), (882, 560))
    screen.blit(font.render(prvni, False, (0, 0, 0)), (880, 560))
    screen.blit(font.render(druhy, False, (150, 150, 150)), (882, 640))
    screen.blit(font.render(druhy, False, (0, 0, 0)), (880, 640))
    screen.blit(font.render(treti, False, (150, 150, 150)), (1052, 560))
    screen.blit(font.render(treti, False, (0, 0, 0)), (1050, 560))
    screen.blit(font.render(ctvrty, False, (150, 150, 150)), (1052, 640))
    screen.blit(font.render(ctvrty, False, (0, 0, 0)), (1050, 640))


def sipecka(screen, imgs, pozice, font, hra):
    prahamon = list(prahadex.prahadex.prahamoni.values())[0]
    abilities = prahamon.abilities
    if pozice == 1:
        screen.blit(imgs.sipkabattle, (840, 570))
        if hra.abilitybattle: pp = f"{abilities[0].pp}/{abilities[0].max_pp}"
    elif pozice == 2:
        screen.blit(imgs.sipkabattle, (840, 650))
        if hra.abilitybattle: pp = f"{abilities[1].pp}/{abilities[1].max_pp}"
    elif pozice == 3:
        screen.blit(imgs.sipkabattle, (1010, 570))
        if hra.abilitybattle: pp = f"{abilities[2].pp}/{abilities[2].max_pp}"
    elif pozice == 4:
        screen.blit(imgs.sipkabattle, (1010, 650))
        if hra.abilitybattle: pp = f"{abilities[3].pp}/{abilities[3].max_pp}"
    if hra.abilitybattle:
        screen.blit(font.render(f"PP: {pp}", True, (150, 150, 150)), (112, 660))
        screen.blit(font.render(f"PP: {pp}", True, (0, 0, 0)), (110, 660))


def handle(hra, event):
    prahamon = list(prahadex.prahadex.prahamoni.values())[0]
    if not hra.protivnici:
        return
    protivnik = hra.protivnici[hra.protivnik_index]
    abilities = prahamon.abilities

    if not hra.show_inventar:
        if event.key == pygame.K_a and not hra.abilitybattle:
            if hra.pozice > 1:
                hra.pozice -= 1
            elif hra.pozice == 1:
                hra.pozice = 4
        elif event.key == pygame.K_a and hra.abilitybattle:
            if hra.pozice > 1:
                hra.pozice -= 1
            elif hra.pozice == 1:
                hra.pozice = len(abilities)

        if event.key == pygame.K_d and not hra.abilitybattle:
            if hra.pozice < 4:
                hra.pozice += 1
            elif hra.pozice == 4:
                hra.pozice = 1
        elif event.key == pygame.K_d and hra.abilitybattle:
            if hra.pozice < len(abilities):
                hra.pozice += 1
            elif hra.pozice == len(abilities):
                hra.pozice = 1

        if event.key == pygame.K_e and not hra.abilitybattle:
            if hra.pozice == 1:
                hra.abilitybattle = True
            elif hra.pozice == 3:
                hra.show_inventar = True
            elif hra.pozice == 4:
                hra.battle = False
        elif event.key == pygame.K_e and hra.abilitybattle:
            if hra.pozice == 1:
                protivnik.hp -= abilities[0].damage
                abilities[0].pp -= 1
            if hra.pozice == 2:
                protivnik.hp -= abilities[1].damage
                abilities[1].pp -= 1
            if hra.pozice == 3:
                protivnik.hp -= abilities[2].damage
                abilities[2].pp -= 1
            if hra.pozice == 4:
                protivnik.hp -= abilities[3].damage
                abilities[3].pp -= 1
            if protivnik.hp <= 0:
                protivnik.hp = 0
                hra.abilitybattle = False
                if hra.protivnik_index < len(hra.protivnici) - 1:
                    hra.protivnik_index += 1
                else:
                    hra.battle = False
        if event.key == pygame.K_ESCAPE:
            if hra.abilitybattle:
                hra.abilitybattle = False
