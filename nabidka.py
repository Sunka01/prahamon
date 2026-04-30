
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
