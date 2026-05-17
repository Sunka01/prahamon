import npc
import predmety
import databaze
import nastaveni as imgs

locations = {
    "Praha": {
        "map": "map.tmx",
        "npcs": [
            npc.Npc("oak", imgs.oak, 1620, 1420, dialog=databaze.dialog1),
            npc.Npc("babisek", imgs.babisek, 1660, 1420, dialog=databaze.dialog2),
            npc.Npc("cong", imgs.cong, 300, 200),
            npc.Npc("doctor", imgs.doctor, 300, 600, dialog="Chces vylecit sve Prahamony?")
        ],
        "predmety": [
            predmety.Predmet("Prahaball", imgs.prahaball, 1620, 1220),
            predmety.Predmet("Pivko", imgs.pivko, 1520, 1220),
        ],
    },
    "Viden": {
        "map": "untitled.tmx",
        "npcs": [npc.Npc("cong", imgs.cong, 1000, 800),
                 npc.Npc("doctor", imgs.doctor, 300, 600, dialog="Chces vylecit sve Prahamony?")],
        "predmety": [],
    }
}
