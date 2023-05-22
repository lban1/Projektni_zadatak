from abc import ABC,abstractmethod
class Korisnik(ABC):
    def __init__(self, tel, email):
        self._tel = tel
        self._email = email
    @property
    def tel(self):
        return self._tel

    @property
    def email(self):
        return self._email

    @abstractmethod
    def ispis(self):
        pass

class PrivatniKorisnik(Korisnik):
    def __init__(self, tel, email, ime, prezime):
        super().__init__(tel, email)
        self.__ime = ime
        self.__prezime = prezime

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    def ispis(self):
        print(f'Informacije o privatnom korisniku:')
        print(f'\tIme: {self.__ime}')
        print(f'\tPrezime: {self.__prezime}')
        print(f'\tTelefon: {self.tel}')
        print(f'\tEmail: {self.email}')

class PoslovniKorisnik(Korisnik):
    def __init__(self, tel, email, naziv, web,):
        super().__init__(tel, email)
        self.__naziv = naziv
        self.__web = web

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def web(self):
        return self.__web

    @web.setter
    def web(self, web):
        self.__web = web

    def ispis(self):
        print(f'Informacije o poslovnom korisniku:')
        print(f'\tNaziv: {self.__naziv}')
        print(f'\tWeb: {self.__web}')
        print(f'\tTelefon: {self.tel}')
        print(f'\tEmail: {self.email}')