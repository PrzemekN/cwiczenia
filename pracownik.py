class Pracownik:
    ilosc_pracownikow = 0
    przyrost_wartosc = 1.04

    def __init__(self, imie: str, nazwisko: str, zarobki: int = 0) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.zarobki = zarobki
        Pracownik.ilosc_pracownikow += 1

    def drukuj_pelne_nazwisko(self) -> None:
        print(f"{self.imie} {self.nazwisko}")

    def pelne_nazwisko(self) -> str:
        return f"{self.imie} {self.nazwisko}"

    #  ********** METODY CLASOWE / CLASS METHOD **********
    @classmethod  # dodajemy dekorator
    def set_przyrost_wartosci(cls, wielkosc: float) -> None:  # cls bedzie przyjmowało klase a nie instancje.
        cls.przyrost_wartosc = wielkosc

    # pytanie: czy z pozimu zwyklej funkcji mozemy zmieniac zmienną klasową, np przyrost_wartosci?
    # metode klasowa mozesz takze wywołać z instancji obiektu- jednak generalnie tak sie nie powinno robic.
    # Uwaga jesli z instancji klasy odwolasz sie do zmiennej klasowej np prac1.przyrost_wart to powstanie nowa zmienna
    # w instancji klasy o takiej samej nazwie jak zmienna klasowa ale nie bedzie to zmienna klasowa!!!

    # ********** CLASS METHODS JAKO ALTERNATYWNY KONSTRUKTOR **********
    # czyli jak stworzyć nasz obiekt (instancje klasy) w inny sposób tzn za pomoca class methods?
    # zerknij na modul datetime w ktorym wykorzystuje sie to podejście.

    @classmethod
    def from_prac_str(cls, prac_str: str):  # jest zasada,ze nazwy alternatywnych konstrukt. rozpoczyna się od "from"
        imie, nazwisko, zarobki = prac_str.split(";")  # tu trzeba miec pewnosc ze split podzieli na 3 elementy?
        return cls(imie, nazwisko, zarobki)  # zauważ ze wywolujemy konstruktor init

    # ********** METODY STATYCZNE / STATIC METHODS **********
    # statyczne metody nie przekazuja ani instancji: self ani klasy: cls,
    # nie zależa od żadnej istnscji klasowej ani od zadnej klasy i sie do nich w ciale klasy nie odwolują.
    @staticmethod
    def dodawanie(arg1, arg2):
        return arg1 + arg2


prac_1 = Pracownik("Przemek", "Nawrocki", 8000)
prac_2 = Pracownik("Magda", "Nawrocka", 9000)
ciag = "Kamila;Nawrocka;10000"
prac_3 = Pracownik.from_prac_str(ciag)
prac_4 = Pracownik("Bartosz", "Nawrocki")
prac_5 = Pracownik(nazwisko="SerDeGiel", imie="Winktoria", zarobki=9000)

Pracownik.set_przyrost_wartosci(1.05)
Pracownik.przyrost_wartosc = 1
print(prac_1.przyrost_wartosc)
print(prac_2.przyrost_wartosc)
print(Pracownik.przyrost_wartosc)
print(Pracownik.dodawanie(1, 3))
Pracownik.przyrost_wartosc = 2
Pracownik.set_przyrost_wartosci(3)
pass
