# megoldás

jatekos_lapok = [2, 3, 4]
gep_lapok = [10, 4, 10]
# nem érem el jelenleg ezeket


def eredmeny(jatekos_lapok: [int], gep_lapok: [int], osszeg):
    jatekos_pontok: [int] = pontszamitas(osszeg)
    gep_pontok: [int] = pontszamitas(osszeg)

    if jatekos_pontok > 21:
        print("Játékos vesztett!")
    elif gep_pontok > 21:
        print("Gép vesztett!")
    else:
        print("LEfutott")


def pontszamitas(lapok: [list]):
    osszeg = 0
    for i in range(len(lapok)):
        osszeg = osszeg + lapok[i]
    return osszeg

# teszt esetek

# nem hívtad meg azért nem irta ki, figyelj jobban
