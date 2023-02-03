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
    print("1.1")
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\nA játékos vesztett")
    else:
        print("A teszt megbukott!\nA játékos nem vesztett")

    print("1.2")
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def jatekos_vesztett_egyenlo():
    jatekos_lista = [6, 4, 8, 9]
    gep_lista = [6, 4, 11]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    print("\nGép vesztett egyenlő teszt :")
    print("2.1.")
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\nEgyenlő")
    else:
        print("A teszt megbukott!\nNem egyenlő")

    jatekos_lista = [6, 4, 8]
    gep_lista = [6, 4, 11]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    print("2.1.")
    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres!\nNem egyenlő")
    else:
        print("A teszt megbukott!\nEgyenlő")


def gep_vesztett_teszt():
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    print("\nGép vesztett teszt eredménye: ")
    print("3.1")
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\n A gép vesztett")
    else:
        print("A teszt megbukott!\n A gép nem vesztett")

    print("3.2")
    jatekos_lista = [6, 4, 8, 9]
    gep_lista = [6, 4, 11]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def jatekos_nyer_teszt():
    jatekos_lista = [6, 4, 8, 2]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    print("\nA játékos nyert teszt")
    print("4.1")
    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres! \nA játékos nyert!")
    else:
        print("A teszt megbukott!\nA játékos nem nyert!")

    print("4.1")
    jatekos_lista = [6, 4, 6]
    gep_lista = [6, 4, 8, 2]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"
    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")

def tesztek():
    jatekos_vesztett_teszt()
    jatekos_vesztett_egyenlo()
    gep_vesztett_teszt()



tesztek()
