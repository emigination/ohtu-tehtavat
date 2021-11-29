from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self._ostokset:
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset:
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi()==lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        poistettava_ostos = None
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi()==poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara()<1:
                    poistettava_ostos = ostos
        if poistettava_ostos:
            self._ostokset.remove(poistettava_ostos)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

    def _ostosten_nimet(self):
        nimet = []
        for ostos in self._ostokset:
            nimet.append(ostos.tuotteen_nimi())
        return nimet
