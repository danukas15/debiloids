import json
import random

# Randomizeris, isrenka is visu galimu viena, pvz is breakfast gauna kiausiniene

# (Dar butu smagu kad tam tikri turetu didesni sansa)
# -- Faila koreguok jai nori tokiu bet ciuju nevarke
# atrinkimas, kad nebutu tas pats patiekalas per breakfast ir snack ir t.t.
# Dar bus directory.
Kiek_Valgyt = {
    "kiausiniene": 3,
}
# kas cia bbz
# zek json fila

with open("products.json") as f:
    obj = json.load(f)

    dayMenu = [
        random.choice(obj["breakfast"]),
        random.choice(obj["snack"]),
        random.choice(obj["lunch"]),
    ]

    while len(dayMenu) != len(set(dayMenu)):
        dayMenu = [
            random.choice(obj["breakfast"]),
            random.choice(obj["snack"]),
            random.choice(obj["lunch"]),
        ]

    print(*dayMenu, sep="\n")
