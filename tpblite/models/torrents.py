import re
import unicodedata
import lxml.etree as ET


def fileSizeStrToInt(size_str):
    """Converts file size given in *iB format to bytes integer"""

    unit_dict = {
        "B": 1,
        "KiB": (2 ** 10),
        "MiB": (2 ** 20),
        "GiB": (2 ** 30),
        "TiB": (2 ** 40),
    }
    try:
        (num, unit) = size_str.split()
        return int(float(num) * unit_dict[unit])
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
        self.upload_date, self.filesize, self.uploader = self._getFileInfo()
        self.byte_size = self._getByteSize()
        self.magnetlink = self._getMagnetLink()
        self.url = self._getUrl()
        self.is_vip = self._getVip()
        self.is_trusted = self._getTrusted()
        self.infohash = self._getInfohash()
        self.category = self._getCategory()

    def __str__(self):
        return "{0}, S: {1}, L: {2}, {3}".format(
            self.title, self.seeds, self.leeches, self.filesize
        )

    def __repr__(self):
        return "<Torrent object: {}>".format(self.title)

    def _getTitle(self):
        return self.html_row.findtext('.//a[@class="detLink"]')

    def _getMagnetLink(self):
        return self.html_row.xpath('.//a[starts-with(@href, "magnet")]/@href')[0]

    def _getPeers(self):
        taglist = self.html_row.xpath('.//td[@align="right"]/text()')
        return int(taglist[0]), int(taglist[1])

    def _getFileInfo(self):
        text = self.html_row.xpath('.//font[@class="detDesc"]/descendant::text()')
        text = ''.join(text)
        t = text.split(",")
        uptime = unicodedata.normalize("NFKD", t[0].replace("Uploaded ", "").strip())
        size = unicodedata.normalize("NFKD", t[1].replace("Size ", "").strip())
        uploader = unicodedata.normalize("NFKD", t[2].replace("ULed by ", "").strip())
        return uptime, size, uploader

    def _getByteSize(self):
        return fileSizeStrToInt(self.filesize)

    def _getUrl(self):
        tag = self.html_row.find('.//a[@class="detLink"]')
        return tag.get("href")

    def _getVip(self):
        image_name = self.html_row.xpath('.//img/@src')[1]
        return 'vip' in image_name

    def _getTrusted(self):
        image_name = self.html_row.xpath('.//img/@src')[1]
        return 'trusted' in image_name

    def _getInfohash(self):
        infohash = re.search(r'btih:(.*?)&dn', self.magnetlink)
        return infohash.group(1) if infohash else None

    def _getCategory(self):
        taglist = self.html_row.xpath('.//a[@title="More from this category"]/text()')
        return '{} -> {}'.format(taglist[0], taglist[1]) if len(taglist) == 2 else None


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
        root = ET.HTML(self.html_source)
        if root.find("body") is None:
            raise ConnectionError("Could not determine torrents (empty html body)")
        rows = root.xpath('//tr[td[@class="vertTh"]]')
        torrents = []
        for row in rows:
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
