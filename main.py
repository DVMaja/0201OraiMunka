# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_pontok: [int] = pontszamitas(jatekos_lapok)
    gep_pontok: [int] = pontszamitas(gep_lapok)
    kiirando = ""

    if jatekos_pontok > 21:
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
def jatekos_nyer():
    jatekos_lista = [6, 4, 8, 2]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett!"

    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres! \tA játékos nyert!")
    else:
        print("A teszt megbukott!\tA játékos nem nyert!")


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
def gep_nyer():
    jatekos_lista = [6, 4, 6, 10]
    gep_lista = [6, 4, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"

    if kapott_eredmeny != vart_eredmeny:
        print("A teszt sikeres! \tGép nyer, játékos nem nyert!")
    else:
        print("A teszt megbukott!\tGép nem nyer!")


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
def dontetlen():
    jatekos_lista = [6, 4, 8]
    gep_lista = [6, 4, 8]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"
    vart_eredmeny2 = "Játékos vesztett!"

    if (kapott_eredmeny != vart_eredmeny) and (kapott_eredmeny != vart_eredmeny2):
        print("A teszt sikeres!\tDöntetlen!!")
    else:
        print("A teszt megbukott!\tNem teljes döntetlen")


def dontetlen_mindeni_veszit():
    jatekos_lista = [6, 4, 6, 10]
    gep_lista = [6, 4, 6, 10]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"
    kapott_eredmeny2 = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny2 = "Játékos vesztett!"

    if (kapott_eredmeny == vart_eredmeny) and (kapott_eredmeny2 == vart_eredmeny2):
        print("A teszt sikeres!\tDöntetlen, mindenki vesztett!!")
    else:
        print("A teszt megbukott!\tNem teljes veszteség!")

# Mindenki nyer


def mindenki_nyer():
    jatekos_lista = [6, 4, 6, 5]
    gep_lista = [6, 4, 6, 5]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett!"
    kapott_eredmeny2 = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny2 = "Játékos vesztett!"

    if (kapott_eredmeny != vart_eredmeny) and (kapott_eredmeny2 != vart_eredmeny2):
        print("A teszt sikeres!\tDöntetlen, mindenki nyert!!")
    else:
        print("A teszt megbukott!\tNem teljes nyereség!")


def tesztek():
    # 9 teszt kb
    jatekos_nyer()
    jatekos_veszit_21tul()
    jatekos_veszit_gepNy()

    gep_nyer()
    gep_veszit_21tul()
    gep_veszit_jatekosNy()

    dontetlen()
    dontetlen_mindeni_veszit()

    mindenki_nyer()
tesztek()
