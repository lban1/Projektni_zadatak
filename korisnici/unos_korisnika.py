from .korisnik import PrivatniKorisnik, PoslovniKorisnik
from utilities import unos_telefona, unos_intervala
def unos_korisnika(redni_b):

    #Definiranje rijecnika
    #korisnik = {}

    #Upis trazenih podataka od korisnika
    """
    korisnik['ime'] = input(f'Unesite ime {redni_b}. korisnika: ')
    korisnik['ime'] = korisnik['ime'].strip()
    korisnik['ime'] = korisnik['ime'].capitalize()

    korisnik['prezime'] = input(f'Unesite prezime {redni_b}. korisnika: ')
    korisnik['prezime'] = korisnik['prezime'].strip()
    korisnik['prezime'] = korisnik['prezime'].capitalize()

    korisnik['tel'] = unos_pozitivnog_cijelog_broja(f'Unesite telefonski broj {redni_b}. korisnika: ')

    korisnik['email'] = input(f'Unesite e-mail {redni_b}. korisnika: ')
    korisnik['email'] = korisnik['email'].strip()
    """

    tel = unos_telefona(f'Unesite telefonski broj {redni_b}. korisnika: ')
    email = input(f'Unesite e-mail {redni_b}. korisnika: ').strip()
    print(f'Odabir vrste korisnika: ')
    print("\t 1. Poslovni korisnik")
    print("\t 2. Privatni korisnik")

    odabir_korisnika = unos_intervala(1,2)

    if odabir_korisnika == 1:
        naziv = input(f'Unesite naziv {redni_b}. korisnika: ')
        web = input(f'Unesite web stranicu {redni_b}. korisnika: ')

        return PoslovniKorisnik(tel, email, naziv, web)

    elif odabir_korisnika == 2:
        ime = input(f'Unesite ime {redni_b}. korisnika: ').strip().capitalize()
        prezime = input(f'Unesite prezime {redni_b}. korisnika: ').strip().capitalize()

        return PrivatniKorisnik(tel, email, ime, prezime)