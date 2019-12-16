import random
from urllib.request import Request, urlopen
from purl import URL as pURL


class QueryParser(object):
    '''
    Query object capable of getting html response given 
    a search query and other parameters.
    '''
    def __init__(self, query, base_url, page, order, category):
        self.base_url = base_url
        segments = ('search', query, str(page), str(order), str(category))
        self.url = URL(base_url, segments)
        self.html_source = self._sendRequest()
     
    def _sendRequest(self):
        req = Request(self.url, headers=headers())
        return urlopen(req).read()

def URL(base, segments):
    u = pURL().from_string(base)
    url = u.path_segments(segments)
    return url.as_string()


def headers():
    '''
    The Pirate Bay blocks requests (403 Forbidden)
    basing on User-Agent header, so it's probably better to rotate them.
    User-Agents taken from:
    https://techblog.willshouse.com/2012/01/03/most-common-user-agents/
    '''
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "origin_req_host": "thepiratebay.se",
    }


USER_AGENTS = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
)

### ====================