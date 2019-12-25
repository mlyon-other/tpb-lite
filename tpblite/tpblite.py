from typing import Optional

from .models.torrents import Torrents, Torrent
from .models.utils import QueryParser


class TPB:

    def __init__(self, base_url: str = "https://tpb.party"):
        """ThePirateBay Object

        Args:
            base_url (str): PirateBay URL to use for queries

        """
        # PirateBay URL to use for queries
        self.base_url = base_url

        # Compiled search string used to query the PirateBay URL
        self._search_url: Optional[str] = None

    def __str__(self) -> str:
        return "TPB Object, base URL: {}".format(self.base_url)

    def search(
        self, query: str, page: int = 0, order: int = 99, category: int = 0
    ) -> Torrents:
        """Search ThePirateBay and return list of Torrents

        Args:
            query: Search string to query ThePirateBay
            page: Page number to grab results from
            order: Order of results, default is ascending. List of possible options found in
                tpblite.models.constants.ORDERS
            category: Restrict search to specific category, for list of categories see
                tpblite.models.constants.CATEGORIES

        Return:
            Torrents object

        """
        q = QueryParser.search(query, self.base_url, page, order, category)
        self._search_url = q.url
        return Torrents(q.html_source)

    def browse(self, category: int = 0, page: int = 0, order: int = 99) -> Torrents:
        """Browse ThePirateBay and return list of Torrents

        Args:
            query: Search string to query ThePirateBay
            page: Page number to grab results from
            order: Order of results, default is ascending. List of possible options found in
                tpblite.models.constants.ORDERS
            category: Restrict search to specific category, for list of categories see
                tpblite.models.constants.CATEGORIES

        Return:
            Torrents object

        """
        q = QueryParser.browse(self.base_url, category, page, order)
        self._search_url = q.url
        return Torrents(q.html_source)
