import json
import os

import inventar
import npc
import prahadex

save = "save.json"


def ulozit(hra):
    prahamoni = []
    for p in prahadex.prahadex.prahamoni.values():
        abilities = []
        for a in p.abilities:
            abilities.append({"name": a.name, "damage": a.damage, "pp": a.pp, "max_pp": a.max_pp})
        prahamoni.append({"name": p.name, "hp": p.hp, "maxhp": p.maxhp, "lvl": p.lvl, "abilities": abilities})

    data = {"x": hra.x, "y": hra.y, "penize": hra.penize, "inventar": inventar.inventory.items, "prahamoni": prahamoni,
            "lokace": hra.nactena}
    with open(save, "w") as f:
        json.dump(data, f, indent=2)


def nacist(hra):
    if not os.path.exists(save):
        return
    with open(save, "r") as f:
        data = json.load(f)
    hra.x = data["x"]
    hra.y = data["y"]
    hra.penize = data["penize"]
    inventar.inventory.items = data.get("inventar", {})
    prahadex.prahadex.prahamoni.clear()
    for p in data.get("prahamoni", []):
        abilities = [npc.Ability(a["name"], a["damage"], a["pp"], a["max_pp"]) for a in p["abilities"]]
        prahamon = npc.Prahamon(p["name"], p["hp"], p["maxhp"], p["lvl"], abilities)
        prahadex.prahadex.add(prahamon)

        # Tady to savuje lokaci a taky portales sou vyjebany hardem takze to budu asi muset udelat pres nejakej dictionary nebo neco idk
        # ale zatim to funguje
    hra.lokaceload(data["lokace"])
    if data["lokace"] == "Viden":
        hra.portalPVx = 40
        hra.portalPVy = 70
