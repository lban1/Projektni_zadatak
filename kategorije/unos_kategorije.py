from artikli import unos_artikla

def unos_kategorije(redni_b):
    #Definiranje rijecnika
    kategorija={}

    #Upis trazenih podataka od korisnika
    kategorija['ime_kategorije']=input(f'Unesite ime {redni_b}. kategorije: ')

    # Definiranje praznog polja
    kategorija['artikli'] = []

    #Definiranje broja artikala
    n_artikla = int(input(f'Unesite broj artikala za {redni_b}. kategoriju: '))

    #Uz pomoc for petlje upisati artikle
    for i in range(1, n_artikla + 1):
        artikl = unos_artikla(i)
        kategorija['artikli'].append(artikl)

    return kategorija