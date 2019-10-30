import random
from urllib.request import Request, urlopen

# Delete these when finished rewriting URL
from collections import OrderedDict
from purl import URL as PURL
# ==============================

class Query(object):
    '''
    Query object capable of getting html response given 
    a search query and other parameters.
    '''
    def __init__(self, query, base_url='https://tpb.party', page=0, order=99, category=0):
        self.base_url = base_url
        self.base_path = '/search'
        self.url = URL(base_url, self.base_path,
                       segments=['query', 'page', 'order', 'category'],
                       defaults=[query, str(page), str(order), str(category)],
                       )
        self.webpage = self._sendRequest()
    
    def _sendRequest(self):
        req = Request(self.url, headers=headers())
        return urlopen(req).read()


### REWRITE THEN DELETE THESE

def URL(base, path, segments=None, defaults=None):
    """
    URL segment handler capable of getting and setting segments by name. The
    URL is constructed by joining base, path and segments.

    For each segment a property capable of getting and setting that segment is
    created dynamically.
    """
    # Make a copy of the Segments class
    url_class = type(Segments.__name__, Segments.__bases__,
                     dict(Segments.__dict__))
    segments = [] if segments is None else segments
    defaults = [] if defaults is None else defaults
    # For each segment attach a property capable of getting and setting it
    for segment in segments:
        setattr(url_class, segment, url_class._segment(segment))
    # Instantiate the class with the actual parameters
    return url_class(base, path, segments, defaults)


class Segments(object):

    """
    URL segment handler, not intended for direct use. The URL is constructed by
    joining base, path and segments.
    """

    def __init__(self, base, path, segments, defaults):
        # Preserve the base URL
        self.base = PURL(base, path=path)
        # Map the segments and defaults lists to an ordered dict
        self.segments = OrderedDict(zip(segments, defaults))

    def build(self):
        # Join base segments and segments
        segments = self.base.path_segments() + tuple(self.segments.values())
        # Create a new URL with the segments replaced
        url = self.base.path_segments(segments)
        return url

    def __str__(self):
        return self.build().as_string()

    def _get_segment(self, segment):
        return self.segments[segment]

    def _set_segment(self, segment, value):
        self.segments[segment] = value

    @classmethod
    def _segment(cls, segment):
        """
        Returns a property capable of setting and getting a segment.
        """
        return property(
            fget=lambda x: cls._get_segment(x, segment),
            fset=lambda x, v: cls._set_segment(x, segment, v),
        )


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