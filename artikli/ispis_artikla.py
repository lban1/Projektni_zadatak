def ispis_artikla(artikl):
    print('Informacije o artiklu: ')
    print(f'\t Naslov: {artikl["naslov"]}')
    print(f'\t Opis: {artikl["opis"]}')
    print(f'\t Cijena: {artikl["cijena"]}')

def k_odabir_artikla(redni_b, artikl):
    return f"{redni_b}. {artikl['naslov']}"