import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from unittest.mock import Mock, ANY, call


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.ostos = Mock()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(Mock())
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_tuotteen_lisayksen_jalkeen_korin_hinta_oikein(self):
        mock_tuote = Mock()
        mock_tuote.hinta.return_value = 3
        self.kori.lisaa_tuote(mock_tuote)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisayksen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Mock())
        self.kori.lisaa_tuote(Mock())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_korin_hinta_niiden_summa(self):
        mock_tuote1 = Mock()
        mock_tuote1.hinta.return_value = 3
        mock_tuote2 = Mock()
        mock_tuote2.hinta.return_value = 2
        self.kori.lisaa_tuote(mock_tuote1)
        self.kori.lisaa_tuote(mock_tuote2)
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_korissa_kaksi_tavaraa(self):
        mock_tuote = Mock()
        self.kori.lisaa_tuote(mock_tuote)
        self.kori.lisaa_tuote(mock_tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
