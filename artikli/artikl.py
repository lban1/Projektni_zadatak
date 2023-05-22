from abc import ABC, abstractmethod
class Artikl(ABC):
    def __init__(self, naslov, opis, cijena):
        self._naslov = naslov
        self._opis = opis
        self._cijena = cijena

    @property
    def naslov(self):
        return self._naslov
    @naslov.setter
    def naslov(self, naslov):
        self._naslov = naslov

    @property
    def opis(self):
        return self._opis
    @opis.setter
    def opis(self, opis):
        self._opis = opis

    @property
    def cijena(self):
        return self._cijena
    @cijena.setter
    def cijena(self, cijena):
        self._cijena = cijena

    @abstractmethod
    def ispis(self):
        pass

class Vozilo:
    def __izracunaj_kw(self, k_snaga):
        return int(k_snaga*0.735)

    def cijena_osiguranja(self, k_snaga):
        kw = self.__izracunaj_kw(k_snaga)
        return kw*15

class Automobil(Artikl, Vozilo):
    def __init__(self, naslov, opis, cijena, k_snaga):
        super().__init__(naslov, opis, cijena)
        self.k_snaga = k_snaga

    def ispis(self):
        print('Informacije o vozilu: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena}')
        print(f'\t Cijena osiguranja: {self.cijena_osiguranja(self.k_snaga)}')

class Stan(Artikl):
    def __init__(self,naslov, opis, cijena, kvadratura ):
        super().__init__(naslov, opis, cijena)
        self.kvadratura = kvadratura

    def ispis(self):
        print('Informacije o stanu: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena}')
        print(f'\t Kvadratura: {self.kvadratura}')

class Usluga(ABC):
    def cijena_po_satu(self):
        pass

class Instrukcije(Artikl,Usluga):
    def __init__(self, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)

    def cijena_po_satu(self):
        return self.cijena/30

    def ispis(self):
        print('Informacije o instrukcijama: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena_po_satu()}')