import re
import unicodedata
from bs4 import BeautifulSoup

# TODO: write better comments


def fileSizeStrToInt(size_str):
    """Converts file size given in *iB format to bytes integer"""

    unit_dict = {"KiB": (2 ** 10), "MiB": (2 ** 20), "GiB": (2 ** 30), "TiB": (2 ** 40)}
    try:
        num = float(size_str[:-3])
        unit = size_str[-3:]
        return int(num * unit_dict[unit])
    except Exception as e:
        raise AttributeError(
            "Cannot determine filesize: {0}, error: {1}".format(size_str, e)
        )


class Torrent:
    """
    Abstract class to contain info about torrent
    magnet link, file size, number of seeds, number of leeches etc.
    """

    def __init__(self, html_row):
        self.html_row = html_row
        self.title = self._getTitle()
        self.seeds, self.leeches = self._getPeers()
        self.upload_date, self.filesize, self.byte_size, self.uploader = (
            self._getFileInfo()
        )
        self.magnetlink = self._getMagnetLink()

    def __str__(self):
        return "{0}, S: {1}, L: {2}, {3}".format(
            self.title, self.seeds, self.leeches, self.filesize
        )

    def __repr__(self):
        return "<Torrent object: {}>".format(self.title)

    def _getTitle(self):
        return self.html_row.find("a", class_="detLink").string

    def _getMagnetLink(self):
        tag = self.html_row.find("a", href=(re.compile("magnet")))
        link = tag.get("href")
        return link

    def _getPeers(self):
        taglist = self.html_row.find_all("td", align="right")
        return int(taglist[0].string), int(taglist[1].string)

    def _getFileInfo(self):
        text = self.html_row.find("font", class_="detDesc").get_text()
        t = text.split(",")
        uptime = unicodedata.normalize("NFKD", t[0].replace("Uploaded ", "").strip())
        size = unicodedata.normalize("NFKD", t[1].replace("Size ", "").strip())
        byte_size = fileSizeStrToInt(size)
        uploader = unicodedata.normalize("NFKD", t[2].replace("ULed by ", "").strip())
        return uptime, size, byte_size, uploader


class Torrents:
    """
    Torrent object, takes query response and parses into 
    torrent list or dict. Has methods to select items from
    torrent list.
    """

    def __init__(self, html_source):
        self.html_source = html_source
        self.list = self._createTorrentList()

    def __str__(self):
        return "Torrents object: {} torrents".format(len(self.list))

    def __repr__(self):
        return "<Torrents object: {} torrents>".format(len(self.list))

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[index]

    def _createTorrentList(self):
        soup = BeautifulSoup(self.html_source, features="html.parser")
        if soup.body is None:
            raise ConnectionError("Could not determine torrents (empty html body)")
        rows = soup.body.find_all("tr")
        torrents = []
        for row in rows:
            if len(row.find_all("td", {"class": "vertTh"})) == 1:
                torrents.append(Torrent(row))
        return torrents

    def getBestTorrent(self, min_seeds=30, min_filesize="1 GiB", max_filesize="4 GiB"):
        """Filters torrent list based on some constraints, then returns highest seeded torrent
        :param min_seeds (int): minimum seed number filter
        :param min_filesize (str): minimum filesize in XiB form, eg. GiB
        :param max_filesize (str): maximum filesize in XiB form, eg. GiB
        :return Torrent Object: Torrent with highest seed number, will return None if all are filtered out"""
        if not isinstance(min_filesize, int):
            min_filesize = fileSizeStrToInt(min_filesize)
        if not isinstance(max_filesize, int):
            max_filesize = fileSizeStrToInt(max_filesize)
        filtered_list = filter(
            lambda x: self._filterTorrent(x, min_seeds, min_filesize, max_filesize),
            self.list,
        )
        sorted_list = sorted(filtered_list, key=lambda x: x.seeds, reverse=True)
        if len(sorted_list) > 0:
            return sorted_list[0]
        else:
            print("No torrents found given criteria")
            return None

    def _filterTorrent(self, torrent, min_seeds, min_filesize, max_filesize):
        if (
            (torrent.seeds < min_seeds)
            or (torrent.byte_size < min_filesize)
            or (torrent.byte_size > max_filesize)
        ):
            return False
        else:
            return True
