import io
import unittest
import contextlib

from tpblite.models import constants


class ConstantsTestCase(unittest.TestCase):

    def test_categories(self):
        self.assertEqual(constants.CATEGORIES.VIDEO.MOVIES, 201)

    def test_printOptions_one(self):
        sobj = io.StringIO()
        with contextlib.redirect_stdout(sobj):
            constants.ORDERS.NAME.printOptions()
        self.assertEqual(sobj.getvalue(), 'DES\nASC\n')

    def test_printOptions_two(self):
        sobj = io.StringIO()
        with contextlib.redirect_stdout(sobj):
            constants.CATEGORIES.GAMES.printOptions()
        self.assertEqual(
            sobj.getvalue(),
            'ALL\nPC\nMAC\nPSX\nXBOX360\nWII\nHANDHELD\nIOS\nANDROID\nOTHER\n'
        )
        