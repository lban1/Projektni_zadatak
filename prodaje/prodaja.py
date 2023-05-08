class Prodaja:
    def __init__(self, datum, korisnik, artikl, redni_b):
        self.datum = datum
        self.korisnik = korisnik
        self.artikl = artikl
        self.redni_b = redni_b

    def ispis(self):
        print(f'!Informacije o {self.redni_b}.prodaji!')
        self.korisnik.ispis()
        self.artikl.ispis()
        print(f'Datum isteka prodaje:')
        print(f'\t Dan: {self.datum.day}')
        print(f'\t Mjesec: {self.datum.month}')
        print(f'\t Godina: {self.datum.year}')
        print('-' * 20)