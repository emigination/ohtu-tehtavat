class Komento:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

class Summa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self._sovelluslogiikka.plus(int(self.lue_syote()))

class Erotus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self._sovelluslogiikka.miinus(int(self.lue_syote()))

class Nollaus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self._sovelluslogiikka.kumoa()
