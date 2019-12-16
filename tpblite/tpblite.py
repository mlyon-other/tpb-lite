from .models.torrents import Torrents, Torrent
from .models.utils import QueryParser

class TPB(object):
    
    def __init__(self, base_url='https://tpb.party'):
        '''ThePirateBay Object

        Args:
            base_url (str): PirateBay URL to use for queries

        Attributes:
            search_url (str): This is the compiled search string used
                to query the PirateBay URL, modified when calling search
                method
        '''
        self.base_url = base_url
        self.search_url = None
        
    def __str__(self):
        return 'TPB Object, base URL: {}'.format(self.base_url)
        
    def search(self, query, page=0, order=99, category=0):
        '''Search ThePirateBay and retturn list of Torrents

        Args:
            query (str): Search string to query ThePirateBay
            page (int): page number to grab results from
            order TODO
            category TODO
        '''
        q = QueryParser(query, self.base_url, page, order, category)
        self.search_url = q.url
        return Torrents(query, q.html_source)