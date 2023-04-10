from artikli import ispis_artikla
from korisnici import ispis_korisnika

def ispis_prodaje(prodaja):
    ispis_korisnika(prodaja['korisnik'])
    ispis_artikla(prodaja['artikl'])

    print('Datum isteka prodaje:')
    print(f'\t Dan: {prodaja["datum"].day}')
    print(f'\t Mjesec: {prodaja["datum"].month}')
    print(f'\t Godina: {prodaja["datum"].year}')
    print('-' * 20)