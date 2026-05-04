import prahadex
import nastaveni as imgs




def draw(screen, font, hra):
    prahamon = list(prahadex.prahadex.prahamoni.values())[0]
    protivnik = hra.protivnici[0]

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

    screen.blit(font.render("Utok", False, (150, 150, 150)), (882, 560))
    screen.blit(font.render("Utok", False, (0, 0, 0)), (880, 560))
    screen.blit(font.render("PD", False, (150, 150, 150)), (882, 640))
    screen.blit(font.render("PD", False, (0, 0, 0)), (880, 640))
    screen.blit(font.render("Inventar", False, (150, 150, 150)), (1052, 560))
    screen.blit(font.render("Inventar", False, (0, 0, 0)), (1050, 560))
    screen.blit(font.render("Run", False, (150, 150, 150)), (1052, 640))
    screen.blit(font.render("Run", False, (0, 0, 0)), (1050, 640))


def sipecka(screen, imgs, pozice):
    if pozice == 1:
        screen.blit(imgs.sipkabattle, (840, 570))
    elif pozice == 2:
        screen.blit(imgs.sipkabattle, (840, 650))
    elif pozice == 3:
        screen.blit(imgs.sipkabattle, (1010, 570))
    elif pozice == 4:
        screen.blit(imgs.sipkabattle, (1010, 650))
