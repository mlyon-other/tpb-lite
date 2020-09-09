import unittest

from tpblite import TPB

class TPBTestCase(unittest.TestCase):

    def test_str(self):
        t = TPB('https://tpb.party')
        self.assertEqual(str(t), 'TPB Object, base URL: https://tpb.party')
