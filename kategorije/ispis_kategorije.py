from artikli import ispis_artikla
def k_odabir_kategorije(redni_b, kategorija):
    return f"{redni_b}.  {kategorija['ime_kategorije']}"

def ispis_svih_kategorija(kategorije, x):
    for kategorija in kategorije:
        x = x+1
        y = 0
        print(f'{x}. {kategorija["ime_kategorije"]}')
        for kategorija['artikl'] in kategorija['artikli']:
            y = y+1
            ispis_artikla(kategorija['artikl'], y)
    x = 0