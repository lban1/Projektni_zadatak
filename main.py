from kategorije import unos_kategorije
from korisnici import unos_korisnika
from prodaje import unos_prodaje, ispis_prodaje

#Definiranje praznih polja

korisnici=[]
kategorije=[]
prodaje=[]

#Definiranje broja korisnika
n_korisnika=int(input('Unesite broj korisnika: '))

#Uz pomoc for petlje upisati korisnike
for i in range(1, n_korisnika+1):

    korisnik = unos_korisnika(i)
    korisnici.append(korisnik)


#Definiranje broja kategorija
n_kategorija=int(input('Unesite broj kategorija: '))

#Uz pomoc for petlje upisati kategorije
for i in range(1, n_kategorija+1):

    kategorija=unos_kategorije(i)
    kategorije.append(kategorija)


#Definiranje broja prodaje
n_prodaja=int(input('Unesite broj prodaja: '))

for i in range(1, n_prodaja+1):

    prodaja=unos_prodaje(korisnici, kategorije, i)
    prodaje.append(prodaja)


for i, prodaja in enumerate(prodaje, start=1):
    print(f'Prodaja {i}')
    ispis_prodaje(prodaja)
