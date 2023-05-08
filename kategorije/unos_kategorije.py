from artikli import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja
from .kategorija import Kategorija

def unos_kategorije(redni_b):
    #Definiranje rijecnika
    #kategorija = {}

    #Upis trazenih podataka od korisnika
    ime_kategorije = input(f'Unesite ime {redni_b}. kategorije: ').capitalize()

    # Definiranje praznog polja
    artikli = []

    #Definiranje broja artikala
    n_artikla = unos_pozitivnog_cijelog_broja(f'Unesite broj artikala za {redni_b}. kategoriju: ')

    #Uz pomoc for petlje upisati artikle
    for i in range(1, n_artikla + 1):
        artikli.append(unos_artikla(i))

    return Kategorija(ime_kategorije, artikli)