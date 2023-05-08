#Definiranje modula za odabir
from artikli import k_odabir_artikla
from korisnici import k_odabir_korisnika
from kategorije import k_odabir_kategorije
from utilities import  unos_datuma, unos_intervala
from .prodaja import Prodaja

def unos_prodaje(korisnici, kategorije, redni_b):
    # Definiranje rijecnika "prodaja"
    #prodaja = {}

    if len(korisnici) < 1 or len(kategorije) < 1:
        print('!' * 20)
        print('Nije upisano dovoljno informacija za upis prodaje!!')
        print('!' * 20)
        return 0

    datum = unos_datuma()

    # Odabir korisnika
    print(f'Odaberite korisnika {redni_b}. prodaje: ')
    for i, korisnik in enumerate(korisnici, start=1):
        print(k_odabir_korisnika(i,korisnik))

    odabir_korisnik = unos_intervala(1,len(korisnici))
    korisnik = korisnici[odabir_korisnik-1]

    # Odabir kategorije
    print(f'Odaberite kategoriju {redni_b}. prodaje: ')
    for i, kategorija in enumerate(kategorije, start=1):
        print(k_odabir_kategorije(i, kategorija))

    odabir_kategorije = unos_intervala(1,len(kategorije))

    # Odabir artikla
    print(f'Odaberite artikl {redni_b}. prodaje: ')
    for i, artikl in enumerate(kategorije[odabir_kategorije - 1].artikli, start=1):
        print(k_odabir_artikla(i, artikl))

    odabir_artikla = unos_intervala(1,len(kategorije[odabir_kategorije-1].artikli))
    artikl = kategorije[odabir_kategorije-1].artikli[odabir_artikla-1]
    #prodaja['rb'] = redni_b

    return Prodaja(datum, korisnik, artikl, redni_b)