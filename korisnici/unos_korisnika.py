def unos_korisnika(redni_b):

    #Definiranje rijecnika
    korisnik = {}

    #Upis trazenih podataka od korisnika

    korisnik['ime'] = input(f'Unesite ime {redni_b}. korisnika: ')
    korisnik['ime'] = korisnik['ime'].strip()
    korisnik['ime'] = korisnik['ime'].capitalize()

    korisnik['prezime'] = input(f'Unesite prezime {redni_b}. korisnika: ')
    korisnik['prezime'] = korisnik['prezime'].strip()
    korisnik['prezime'] = korisnik['prezime'].capitalize()

    korisnik['tel'] = int(input(f'Unesite telefonski broj {redni_b}. korisnika: '))

    korisnik['email'] = input(f'Unesite e-mail {redni_b}. korisnika: ')
    korisnik['email'] = korisnik['email'].strip()

    return korisnik