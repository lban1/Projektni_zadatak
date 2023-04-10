def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f'\tIme: {korisnik["ime"]}')
    print(f'\tPrezime: {korisnik["prezime"]}')
    print(f'\tTelefon: {korisnik["tel"]}')
    print(f'\tEmail: {korisnik["email"]}')

def k_odabir_korisnika(redni_b, korisnik):
    return f"{redni_b}.  {korisnik['ime']} {korisnik['prezime']}"