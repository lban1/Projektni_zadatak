def ispis_korisnika(korisnik, y):
    print(f'Informacije o korisniku ({y}):')
    print(f'\tIme: {korisnik["ime"]}')
    print(f'\tPrezime: {korisnik["prezime"]}')
    print(f'\tTelefon: {korisnik["tel"]}')
    print(f'\tEmail: {korisnik["email"]}')

def k_odabir_korisnika(redni_b, korisnik):
    return f"{redni_b}.  {korisnik['ime']} {korisnik['prezime']}"

def ispis_svih_korisnika(korisnici, x):
    for korisnik in korisnici:
        x = x+1
        ispis_korisnika(korisnik, x)