from ksp import KSP
from tekoaly import Tekoaly


class KSPTekoaly(KSP):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def pelaa(self):
        super().pelaa()

    def _ensimmaisen_siirto(self):
        return super()._ensimmaisen_siirto()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        return super()._onko_ok_siirto(siirto)

