#Definiranje datuma

from datetime import date

#Definiranje praznih polja

korisnici=[]
kategorije=[]
prodaje=[]

#Definiranje broja korisnika

n_korisnika=int(input('Unesite broj korisnika: '))

#Uz pomoc for petlje upisati korisnike

for i in range(1, n_korisnika+1):

    #Definiranje rijecnika "Korisnik"

    korisnik = {}

    #Upis trazenih podataka od korisnika

    korisnik['ime']=input(f'Unesite ime {i}. korisnika: ')
    korisnik['ime']=korisnik['ime'].strip()
    korisnik['ime']=korisnik['ime'].capitalize()

    korisnik['prezime']=input(f'Unesite prezime {i}. korisnika: ')
    korisnik['prezime']=korisnik['prezime'].strip()
    korisnik['prezime']=korisnik['prezime'].capitalize()

    korisnik['tel']=int(input(f'Unesite telefonski broj {i}. korisnika: '))

    korisnik['email']=input(f'Unesite e-mail {i}. korisnika: ')
    korisnik['email']=korisnik['email'].strip()
    korisnici.append(korisnik)

#print(korisnici)


#Definiranje broja kategorija

n_kategorija=int(input('Unesite broj kategorija: '))

#Uz pomoc for petlje upisati kategorije

for i in range(1, n_kategorija+1):
    kategorija= {}
    artikli=[]

    kategorija['ime_kategorije']=input(f'Unesite ime {i}. kategorije: ')

    # Definiranje broja artikala

    n_artikla=int(input(f'Unesite broj artikala za {i}. kategoriju ({kategorija["ime_kategorije"].capitalize()}): '))

    for j in range(1, n_artikla+1):

        # Definiranje rijecnika "Artikli"

        artikl={}

        #Upis trazenih podataka od korisnika za artikle

        artikl['naslov']=input(f'Unesite naslov {j}. prodajnog artikla: ')
        artikl['naslov']=artikl['naslov'].strip()
        artikl['naslov']=artikl['naslov'].capitalize()

        artikl['opis']=input(f'Unesite svoj opis {j}. prodajnog artikla: ')

        artikl['cijena']=float(input(f'Unesite cijenu {j}. prodajnog artikla (EUR): '))
        artikli.append(artikl)

        #print(artikli)

    kategorija['artikli']=artikli
    kategorije.append(kategorija)

    #print(kategorije)


#Definiranje broja prodaje

n_prodaja=int(input('Unesite broj prodaja: '))

for i in range(1, n_prodaja+1):
    #Definiranje rijecnika "prodaja"
    prodaja = {}

    #Upis trazenih podataka od korisnika
    dan=int(input(f'Unesite dan isteka {i}. prodaje artikla: '))

    #  Provjera ispravnosti upisa
    while dan > 31:
        print('Pogreska unosa, pokusajte ponovo: ')
        dan=int(input())
        if dan <= 31:
            break

    #Upis trazenih podataka od korisnika
    mjesec=int(input(f'Unesite mjesec isteka {i}. prodaje artikla: '))

    #Provjera ispravnosti upisa
    while mjesec > 12:
        print('Pogreska unosa, pokusajte ponovo: ')
        mjesec = int(input())
        if mjesec<=12:
            break

    #Upis trazenih podataka od korisnika
    godina=int(input(f'Unesite godinu isteka {i}. prodaje artikla: '))

    #Definiranje datuma od unesenih podataka
    prodaja['datum']=date(godina, mjesec, dan)

    #Odabir korisnika
    print(f'Odaberite korisnika {i}. prodaje: ')
    for j, korisnik in enumerate(korisnici, start=1):
        print(f'\t{j}. {korisnik["ime"]} {korisnik["prezime"]}')

    odabir_korisnik=int(input('Odabrani korisnik: '))

    #Odabir kategorije
    print(f'Odaberite kategoriju {i}. prodaje: ')
    for j, kategorija in enumerate(kategorije, start=1):
        print(f'\t{j}. {kategorija["ime_kategorije"]}')

    odabir_kategorije = int(input('Odabrana kategorija: '))

    #Odabir artikla
    print(f'Odaberite artikl {i}. prodaje: ')
    for j, artikl in enumerate(kategorije[odabir_kategorije-1]['artikli'], start=1):
        print(f'\t{j}. {kategorije[odabir_kategorije-1]["artikli"][j-1]["naslov"]}')

    odabir_artikla = int(input('Odabrani artikl: '))

    prodaja['korisnik']=korisnici[odabir_korisnik-1]
    prodaja['artikl']=kategorije[odabir_kategorije-1]['artikli'][odabir_artikla-1]
    prodaje.append(prodaja)


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print('Informacije o korisniku: ')
    print(f'\tIme: {prodaja["korisnik"]["ime"]}')
    print(f'\tPrezime: {prodaja["korisnik"]["prezime"]}')
    print(f'\tTelefon: {prodaja["korisnik"]["tel"]}')
    print(f'\tEmail: {prodaja["korisnik"]["email"]}')

    print('Informacije o artiklu: ')
    print(f'\t Naslov: {prodaja["artikl"]["naslov"]}')
    print(f'\t Opis: {prodaja["artikl"]["opis"]}')
    print(f'\t Cijena: {prodaja["artikl"]["cijena"]}')

    print('Datum isteka prodaje: ')
    print(f'\t Dan: {prodaja["datum"].day}')
    print(f'\t Mjesec: {prodaja["datum"].month}')
    print(f'\t Godina: {prodaja["datum"].year}')

    print('-' * 30)



'''
#Upisivanje rijecnika u rijecnik iz kojeg se cita

prodaja['artikl']=artikl
prodaja['korisnik']=korisnik

#Ispis unesenih podataka oglasa

print('Informacije o prodajnom artiklu:')
print('\t Naslov:', prodaja['artikl']['naslov'])
print('\t Opis:', prodaja['artikl']['opis'])
print('\t Cijena:', prodaja['artikl']['cijena'],'EUR')

print('Datum isteka prodaje artikla:')
print('\t Dan:', prodaja['datum'].day)
print('\t Mjesec:', prodaja['datum'].month)
print('\t Godina:', prodaja['datum'].year)

print('Informacije o korisniku:')
print('\t', prodaja['korisnik']['prezime'], prodaja['korisnik']['ime'])
print('\t Telefon:', prodaja['korisnik']['tel'])
print('\t E-mail:', prodaja['korisnik']['email'])
'''