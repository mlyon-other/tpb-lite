from typing import Optional

from .models.torrents import Torrents, Torrent
from .models.utils import QueryParser


class TPB:

    # PirateBay URL to use for queries
    base_url: str

    # Compiled search string used to query the PirateBay URL
    search_url: Optional[str]

    def __init__(self, base_url="https://tpb.party"):
        """ThePirateBay Object

        Args:
            base_url (str): PirateBay URL to use for queries

        """
        self.base_url = base_url
        self.search_url = None

    def __str__(self) -> str:
        return "TPB Object, base URL: {}".format(self.base_url)

    def search(
        self, query: str, page: int = 0, order: int = 99, category: int = 0
    ) -> Torrent:
        """Search ThePirateBay and return list of Torrents

        Args:
            query: Search string to query ThePirateBay
            page: page number to grab results from
            order TODO
            category TODO

        Return:
            Torrent

        """
        q = QueryParser.from_search(query, self.base_url, page, order, category)
        self.search_url = q.url
        return Torrents(q.html_source)

    def browse(
        self, category: int = 0, page: int = 0, order: int = 99
    ) -> Torrent:
        """Browse ThePirateBay and return list of Torrents

        Args:
            query: Search string to query ThePirateBay
            page: page number to grab results from
            order TODO
            category TODO

        Return:
            Torrent

        """
        q = QueryParser.from_browse(self.base_url, category, page, order)
        self.search_url = q.url
        return Torrents(q.html_source)
