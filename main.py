# megoldás

def eredmeny(osszeg):
    pontszamitas(osszeg)
    if osszeg > 21:
        print("Játékos vesztett!")
    elif osszeg > 21:
        print("Gép vesztett!")


def pontszamitas(lista):
    osszeg = 0
    for i in range(lista):
        osszeg = osszeg + lista[i]
    return osszeg

# teszt esetek
