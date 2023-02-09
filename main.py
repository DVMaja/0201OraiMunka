# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_pontok: [int] = pontszamitas(jatekos_lapok)
    gep_pontok: [int] = pontszamitas(gep_lapok)
    kiirando = ""

    if (jatekos_pontok <= 21) and (gep_pontok <= 21):
        if jatekos_pontok > gep_pontok:
            kiirando = "Játékos nyert!"
        elif gep_pontok > jatekos_pontok:
            kiirando = "Gép nyert!"
    elif gep_pontok == jatekos_pontok:
        if len(jatekos_lapok) < len(gep_lapok):
            kiirando = "Játékos nyert!"
        elif len(jatekos_lapok) > len(gep_lapok):
            kiirando = "Gép nyert!."
        else:
            kiirando = "Döntetlen osztoztok a nyereségen."
    elif (jatekos_pontok > 21) and (gep_pontok > 21):
        kiirando = "Döntetlen, a ház nyert."
    elif jatekos_pontok > 21:
        kiirando = "Játékos vesztett!"
    elif gep_pontok > 21:
        kiirando = "Gép vesztett!"
    return kiirando


def pontszamitas(lapok: [list]):
    osszeg = 0
    for i in range(len(lapok)):
        osszeg = osszeg + lapok[i]
    return osszeg


# Teszt esetek
# Játékos tesztek
# Nyer
def jatekos_nyer21_gyel():
    jatekos_lista = [6, 4, 8, 3]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos nyert!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tA játékos nyert!")
    else:
        print("A teszt megbukott!\tA játékos nem nyert!")


def jatekos_nyer19_keves():
    jatekos_lista = [6, 4, 9]
    gep_lista = [6, 4, 6, 2]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos nyert!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tA játékos nyert!")
    else:
        print("A teszt megbukott!\tA játékos nem nyert!")


def jatekos_nyer19_tobb():
    jatekos_lista = [8, 5, 2, 2, 2]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos nyert!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tA játékos nyert!")
    else:
        print("A teszt megbukott!\tA játékos nem nyert!")


# Veszít
def jatekos_veszit_21tul():
    jatekos_lista = [6, 4, 8, 9]
    gep_lista = [6, 4, 11]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\tA játékos vesztett")
    else:
        print("A teszt megbukott!\tA játékos nem vesztett")


def jatekos_veszit_gepNy():
    jatekos_lista = [6, 4, 6, 10]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tA játékos nem nyert, és Gép nyer!")
    else:
        print("A teszt megbukott!\tA játékos nyert, és Gép nem nyer!")


# Gép tesztek
# Nyer
def gep_nyer21_gyel():
    jatekos_lista = [6, 4, 6]
    gep_lista = [6, 4, 6, 5]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép nyert!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tGép nyer, játékos nem nyert!")
    else:
        print("A teszt megbukott!\tGép nem nyer!")


def gep_nyer19_keves():
    jatekos_lista = [6, 4, 6, 2]
    gep_lista = [6, 4, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép nyert!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres! \tGép nyer, játékos nem nyert!")
    else:
        print("A teszt megbukott!\tGép nem nyer!")


def gep_nyer19_tobb():
    jatekos_lista = [6, 4, 6]
    gep_lista = [8, 5, 2, 2, 2]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres! \tGép nyer, játékos nem nyert!")
    else:
        print("A teszt megbukott!\tGép nem nyer!")


# Veszít
def gep_veszit_21tul():
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\tGép vesztett!")
    else:
        print("A teszt megbukott!\tGép nyert!")


def gep_veszit_jatekosNy():
    jatekos_lista = [6, 4, 11]
    gep_lista = [6, 4, 8, 9]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\tGép nyer, játékos nem nyert!")
    else:
        print("A teszt megbukott!\tGép vesztett, és játékos nyert!")


# Döntetlen tesztek
def dontetlen_egyenlo_lsz_ertek():
    jatekos_lista = [6, 4, 8]
    gep_lista = [6, 4, 8]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Döntetlen osztoztok a nyereségen."

    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres!\tDöntetlen egyenlő értékkel és dbszámmal.")
    else:
        print("Teszt sikertelen")


def dontetlen_21tullepve():
    jatekos_lista = [6, 4, 6, 8]
    gep_lista = [6, 4, 6, 10]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Döntetlen, a ház nyert."

    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!\tDöntetlen, mindenki vesztett!!")
    else:
        print("Teszt sikertelen")


def dontetlen_21():
    jatekos_lista = [6, 4, 6, 5]
    gep_lista = [6, 4, 6, 5]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Döntetlen osztoztok a nyereségen."

    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres!\tDöntetlen 21-gyel!")
    else:
        print("Teszt sikertelen")


def tesztek():
    # Játékos tesztek
    jatekos_nyer21_gyel()
    jatekos_nyer19_keves()
    jatekos_nyer19_tobb()

    jatekos_veszit_21tul()
    jatekos_veszit_gepNy()

    # Gép tesztek
    gep_nyer21_gyel()
    gep_nyer19_keves()
    gep_nyer19_tobb()

    gep_veszit_21tul()
    gep_veszit_jatekosNy()

    # Döntetlen tesztek
    dontetlen_egyenlo_lsz_ertek()
    dontetlen_21tullepve()
    dontetlen_21()

tesztek()
