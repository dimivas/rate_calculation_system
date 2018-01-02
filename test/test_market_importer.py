import unittest
import uuid
import numpy

from market_importer import _parse_row, import_csv


class MarketImporterTestSuite(unittest.TestCase):

    def test_parse_row(self):
        res = _parse_row("test", "0.1", "100")
        self.assertIsInstance(res, tuple)
        self.assertEqual(len(res), 3)
        self.assertIsInstance(res[0], uuid.UUID)
        self.assertIsInstance(res[1], float)
        self.assertIsInstance(res[2], int)

    def test_import_csv(self):
        res = import_csv("sample_market_data_files/test.csv")
        self.assertIsInstance(res, numpy.ndarray)