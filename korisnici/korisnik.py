class Korisnik:
    def __init__(self, ime, prezime, tel, email):
        self.__ime = ime
        self.__prezime = prezime
        self.__tel = tel
        self.__email = email

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

    @property
    def tel(self):
        return self.__tel

    @property
    def email(self):
        return self.__email

    def ispis(self):
        print(f'Informacije o korisniku:')
        print(f'\tIme: {self.__ime}')
        print(f'\tPrezime: {self.__prezime}')
        print(f'\tTelefon: {self.__tel}')
        print(f'\tEmail: {self.__email}')