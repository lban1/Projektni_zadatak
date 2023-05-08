class Kategorija:
    def __init__(self, ime_kategorije, artikli):
        self.__ime_kategorije = ime_kategorije
        self.__artikli = artikli

    @property
    def ime_kategorije(self):
        return self.__ime_kategorije
    @ime_kategorije.setter
    def ime_kategorije(self, ime_kategorije):
        self.__ime_kategorije = ime_kategorije

    @property
    def artikli(self):
        return self.__artikli
    @artikli.setter
    def artikli(self, artikli):
        self.__artikli = artikli

    def ispis(self):
        print(f"{self.__ime_kategorije}:")
        for artikl in self.__artikli:
            artikl.ispis()