from ksp import KSP


class KSPPelaajaVsPelaaja(KSP):
    def pelaa(self):
        super().pelaa()

    def _ensimmaisen_siirto(self):
        return super()._ensimmaisen_siirto()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return super()._onko_ok_siirto(siirto)
