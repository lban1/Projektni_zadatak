#Definiranje modula za vrijeme
from datetime import date

#Definiranje modula za odabir
from artikli import k_odabir_artikla
from korisnici import k_odabir_korisnika
from kategorije import k_odabir_kategorije

def unos_prodaje(korisnici, kategorije, redni_b):
    # Definiranje rijecnika "prodaja"
    prodaja={}

    dan = int(input(f'Unesite dan isteka {redni_b}. prodaje artikla: '))

    #  Provjera ispravnosti upisa
    while dan > 31:
        print('Pogreska unosa, pokusajte ponovo: ')
        dan = int(input())
        if dan <= 31:
            break

    # Upis trazenih podataka od korisnika
    mjesec = int(input(f'Unesite mjesec isteka {redni_b}. prodaje artikla: '))

    # Provjera ispravnosti upisa
    while mjesec > 12:
        print('Pogreska unosa, pokusajte ponovo: ')
        mjesec = int(input())
        if mjesec <= 12:
            break

    # Upis trazenih podataka od korisnika
    godina = int(input(f'Unesite godinu isteka {redni_b}. prodaje artikla: '))

    # Definiranje datuma od unesenih podataka
    prodaja['datum'] = date(godina, mjesec, dan)

    # Odabir korisnika
    print(f'Odaberite korisnika {redni_b}. prodaje: ')
    for i, korisnik in enumerate(korisnici, start=1):
        print(k_odabir_korisnika(i,korisnik))

    odabir_korisnik = int(input('Odabrani korisnik: '))
    prodaja['korisnik']=korisnici[odabir_korisnik-1]

    # Odabir kategorije
    print(f'Odaberite kategoriju {redni_b}. prodaje: ')
    for i, kategorija in enumerate(kategorije, start=1):
        print(k_odabir_kategorije(i, kategorija))

    odabir_kategorije = int(input('Odabrana kategorija: '))

    # Odabir artikla
    print(f'Odaberite artikl {redni_b}. prodaje: ')
    for i, artikl in enumerate(kategorije[odabir_kategorije - 1]['artikli'], start=1):
        print(k_odabir_artikla(i, artikl))

    odabir_artikla = int(input('Odabrani artikl: '))

    prodaja['artikl']=kategorije[odabir_kategorije-1]['artikli'][odabir_artikla-1]
    return prodaja