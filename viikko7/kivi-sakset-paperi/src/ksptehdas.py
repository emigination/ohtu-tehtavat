from ksp_parempi_tekoaly import KSPParempiTekoaly
from ksp_pelaaja_vs_pelaaja import KSPPelaajaVsPelaaja
from ksp_tekoaly import KSPTekoaly

class KSPtehdas:
    @staticmethod
    def tehtaile(pelityyppi):
        if pelityyppi == 'kaksinpeli':
            return KSPPelaajaVsPelaaja()
        if pelityyppi == 'haastava':
            return KSPParempiTekoaly()
        return KSPTekoaly()
