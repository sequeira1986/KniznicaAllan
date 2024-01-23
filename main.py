class kniha:
    def __init__(self, nazov, autor, ISBN, dostupna, rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.isbn = ISBN
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania

    def vypozicaj(self):
        if self.dostupna:
            self.dostupna = False
    def vrati(self):
        self.dostupna = True

class Kniznica:
    def __init__(self):
        self.knihy = []
    def pridaj_knihu(self, kniha):

