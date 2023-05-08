from .korisnik import Korisnik
from utilities import unos_telefona
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

    ime = input(f'Unesite ime {redni_b}. korisnika: ').strip().capitalize()
    prezime = input(f'Unesite prezime {redni_b}. korisnika: ').strip().capitalize()
    tel = unos_telefona(f'Unesite telefonski broj {redni_b}. korisnika: ')
    email = input(f'Unesite e-mail {redni_b}. korisnika: ').strip()

    return Korisnik(ime, prezime, tel, email)