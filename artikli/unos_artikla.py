from utilities import unos_pozitivnog_realnog_broja, unos_intervala
from .artikl import Artikl, Automobil, Stan, Instrukcije
def unos_artikla(redni_b):

    #Definiranje rijecnika

    #artikl={}

    #Upis trazenih podataka od korisnika

    '''artikl['naslov'] = input(f'Unesite naslov {redni_b}. prodajnog artikla: ')
    artikl['naslov'] = artikl['naslov'].strip()
    artikl['naslov'] = artikl['naslov'].capitalize()

    artikl['opis'] = input(f'Unesite svoj opis {redni_b}. prodajnog artikla: ')

    artikl['cijena'] = float(input(f'Unesite cijenu {redni_b}. prodajnog artikla (EUR): '))'''

    naslov = input(f'Unesite naslov {redni_b}. prodajnog artikla: ').strip().capitalize()
    opis = input(f'Unesite svoj opis {redni_b}. prodajnog artikla: ')
    cijena = unos_pozitivnog_realnog_broja(f'Unesite cijenu {redni_b}. prodajnog artikla (EUR): ')

    print(f'Odabir vrste artikla: ')
    print("\t 1. Automobil")
    print("\t 2. Stan")
    print("\t 3. Instrukcije")

    odabir_artikla = unos_intervala(1,3)

    if odabir_artikla == 1:
        k_snaga = unos_pozitivnog_realnog_broja(f'{redni_b}. prodajni artikl; Unesite snagu automobila (Ks) : ')

        return Automobil(naslov, opis, cijena, k_snaga)

    elif odabir_artikla == 2:
        kvadratura = unos_pozitivnog_realnog_broja(f'{redni_b}. prodajni artikl; Unesite kvadraturu: ')

        return Stan(naslov, opis, cijena, kvadratura)

    elif odabir_artikla == 3:
        return Instrukcije(naslov, opis, cijena)