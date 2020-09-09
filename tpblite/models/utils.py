from typing import Tuple, Type, TypeVar
import random
from urllib.request import Request, urlopen
from urllib.parse import urlparse, urlunparse, quote
import urllib.error

# https://github.com/python/typing/issues/58#issuecomment-326240794
T = TypeVar("T", bound="QueryParser")


class QueryParser:
    """Query object capable of getting html response given a search query and other
    parameters.
    """

    # PirateBay URL to use for queries
    base_url: str

    # Compiled search string used to query the PirateBay URL
    url: str

    def __init__(self, base_url: str, segments: Tuple[str, ...]):
        self.base_url = base_url
        self.url = URL(base_url, segments)
        try:
            self.html_source = self._sendRequest()
        except urllib.error.URLError:
            raise ConnectionError(
                "Could not establish connection with {}".format(self.url)
            )

    @classmethod
    def search(
        cls: Type[T], query: str, base_url: str, page: int, order: int, category: int
    ) -> T:
        segments = ("search", query, str(page), str(order), str(category))
        return cls(base_url, segments)

    @classmethod
    def browse(cls: Type[T], base_url: str, category: int, page: int, order: int) -> T:
        # The 0 is added to the URL to stay consistent with the manual web request
        segments = ("browse", str(category), str(page), str(order), "0")
        return cls(base_url, segments)

    @classmethod
    def top(cls: Type[T], base_url: str, category: int, last_48: bool) -> T:
        if category == 0:
            category = "all"
        if last_48:
            segments = ("top", "48h" + str(category))
        else:
            segments = ("top", str(category))
        return cls(base_url, segments)

    def _sendRequest(self):
        req = Request(self.url, headers=headers())
        return urlopen(req).read()


def URL(base: str, segments: Tuple[str, ...]) -> str:
    url = list(urlparse(base))
    url[2] = '/'.join((quote(s) for s in segments))
    return urlunparse(url)


def headers():
    """
    The Pirate Bay blocks requests (403 Forbidden)
    basing on User-Agent header, so it's probably better to rotate them.
    User-Agents taken from:
    https://techblog.willshouse.com/2012/01/03/most-common-user-agents/
    """
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "origin_req_host": "thepiratebay.se",
    }


USER_AGENTS = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/60.0.3112.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/60.0.3112.113 Safari/537.36",
)
