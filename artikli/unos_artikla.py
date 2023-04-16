def unos_artikla(redni_b):

    #Definiranje rijecnika

    artikl={}

    #Upis trazenih podataka od korisnika

    artikl['naslov'] = input(f'Unesite naslov {redni_b}. prodajnog artikla: ')
    artikl['naslov'] = artikl['naslov'].strip()
    artikl['naslov'] = artikl['naslov'].capitalize()

    artikl['opis'] = input(f'Unesite svoj opis {redni_b}. prodajnog artikla: ')

    artikl['cijena'] = float(input(f'Unesite cijenu {redni_b}. prodajnog artikla (EUR): '))

    return artikl