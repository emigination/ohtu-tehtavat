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
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_tuotteen_lisayksen_jalkeen_yksi_tavara_korissa(self):
        self.kori.lisaa_tuote(Mock())
        self.assertEqual(self.kori.tavaroita_korissa(),1)

