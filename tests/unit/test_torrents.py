import unittest

from pathlib import Path

from tpblite.models import torrents

DATA_DIR = Path(__file__).parents[1].joinpath('data')

class TorrentsTestCase(unittest.TestCase):

    def setUp(self):
        fobj = open(DATA_DIR.joinpath('torrent_test.html'), 'r')
        contents = fobj.read()
        fobj.close()
        self.torrents = torrents.Torrents(contents)

    def test_str(self):
        self.assertEqual(str(self.torrents), 'Torrents object: 5 torrents')

    def test_repr(self):
        self.assertEqual(repr(self.torrents), '<Torrents object: 5 torrents>')

    def test_length(self):
        self.assertEqual(len(self.torrents), 5)

    def test_title(self):
        self.assertEqual(self.torrents[2].title, 'CBGB 2013 HDRip x264 AC3 UNiQUE')

    def test_seeds(self):
        self.assertEqual(self.torrents[-1].seeds, 500)

    def test_leeches(self):
        self.assertEqual(self.torrents[-1].leeches, 400)

    def test_upload_date(self):
        self.assertEqual(self.torrents[0].upload_date, '4 mins ago')

    def test_uploader(self):
        self.assertEqual(self.torrents[0].uploader, 'Drarbg')

    def test_filesize(self):
        self.assertEqual(self.torrents[1].filesize, '119.24 MiB')

    def test_byte_size(self):
        self.assertEqual(self.torrents[0].byte_size, 3564822855)

    def test_magnetlink(self):
        self.assertEqual(self.torrents[4].magnetlink, 'magnet:?xt=urn:btih:12dce429d8ca04f2b17b28036e11abb2c1239fa6&dn=Fair.Ci')

    def test_url(self):
        self.assertEqual(self.torrents[0].url, '/torrent/8935177/Hot.Wheels.Worlds.Best.Driver-SKIDROW')

    def test_getBestTorrent(self):
        tor = self.torrents.getBestTorrent(min_seeds=50, min_filesize='100 MiB', max_filesize='300 MiB')
        self.assertEqual(tor.title, 'Fair.City.S ')

    def test_getBestTorrentNone(self):
        tor = self.torrents.getBestTorrent()
        self.assertEqual(tor, None)

class TorrentsExceptionsTestCase(unittest.TestCase):

    def test_createTorrentListRaise(self):
        fobj = open(DATA_DIR.joinpath('no_body.html'), 'r')
        contents = fobj.read()
        fobj.close()
        self.assertRaises(ConnectionError, torrents.Torrents, contents)


class TorrentTestCase(unittest.TestCase):

    def setUp(self):
        fobj = open(DATA_DIR.joinpath('torrent_test.html'), 'r')
        contents = fobj.read()
        fobj.close()
        self.torrent = torrents.Torrents(contents)[4]

    def test_str(self):
        self.assertEqual(
            str(self.torrent),
            'Fair.City.S , S: 500, L: 400, 142.17 MiB'
        )

    def test_repr(self):
        self.assertEqual(repr(self.torrent), '<Torrent object: Fair.City.S >')


class fileSizeTestCase(unittest.TestCase):

    def test_raise_one(self):
        self.assertRaises(AttributeError, torrents.fileSizeStrToInt, '400 MiBB')

    def test_raise_two(self):
        self.assertRaises(AttributeError, torrents.fileSizeStrToInt, '400 LiB')

    def test_raise_three(self):
        self.assertRaises(AttributeError, torrents.fileSizeStrToInt, 'm400 MiB')
        


        
    