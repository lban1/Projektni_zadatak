#from artikli import ispis_artikla
#from korisnici import ispis_korisnika

'''def ispis_prodaje(prodaja):
    ispis_korisnika(prodaja['korisnik'], f'{prodaja["rb"]}. prodaje')
    ispis_artikla(prodaja['artikl'], f'{prodaja["rb"]}. prodaje')

    print(f'Datum isteka {prodaja["rb"]} prodaje:')
    print(f'\t Dan: {prodaja["datum"].day}')
    print(f'\t Mjesec: {prodaja["datum"].month}')
    print(f'\t Godina: {prodaja["datum"].year}')
    print('-' * 20)'''

def ispis_svih_prodaja(prodaje):
    for prodaja in prodaje:
        prodaja.ispis()