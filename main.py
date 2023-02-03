# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_pontok: [int] = pontszamitas(jatekos_lapok)
    gep_pontok: [int] = pontszamitas(gep_lapok)
    kiirando = ""

    if jatekos_pontok > 21:
        kiirando = "Játékos vesztett!"
    elif gep_pontok > 21:
        kiirando = "Gép vesztett!"
    else:
        kiirando = "LEfutott"
    return kiirando


def pontszamitas(lapok: [list]):
    osszeg = 0
    for i in range(len(lapok)):
        osszeg = osszeg + lapok[i]
    return osszeg


# Teszt esetek

def jatekos_vesztett_teszt():
    jatekos_lista = [6, 4, 8, 9]
    gep_lista = [6, 4, 11]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    print("\nJátékos vesztett teszt eredményei:")
    print("1. A teszt sikeres")
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")

    print("\n2.A teszt sikertelen")
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def gep_vesztett_teszt():
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"
    print("\nGép vesztett teszt eredménye: ")
    print("1. A teszt sikeres")
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    elif len(jatekos_lista) == len(gep_lista):
        print("Egyenlő számú lapjuk van.")
    else:
        print("A teszt megbukott!")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()


tesztek()
