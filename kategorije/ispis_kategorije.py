from artikli import ispis_artikla
def k_odabir_kategorije(redni_b, kategorija):
    return f"{redni_b}.  {kategorija.ime_kategorije}"

def ispis_svih_kategorija(kategorije):
    for kategorija in kategorije:
        print(f'{kategorija.ime_kategorije}:')
        for artikl in kategorija.artikli:
            artikl.ispis()