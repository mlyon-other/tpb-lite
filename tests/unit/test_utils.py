import unittest

from tpblite.models import utils


class URLTestCase(unittest.TestCase):
    def test_URL(self):
        self.assertEqual(
            utils.URL('https://some.domain', ('1', '99', '200')),
            'https://some.domain/1/99/200'
        )
