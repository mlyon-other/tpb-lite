from .models.torrents import Torrents, Torrent
from .models.utils import Query

class TPB(object):
    
    def __init__(self, base_url='https://tpb.party'):
        self.base_url = base_url
        self.search_url = None
        
    def __str__(self):
        return 'TPB Object, base URL: {}'.format(self.base_url)
        
    def search(self, query, page=0, order=99, category=0):
        q = Query(query, self.base_url, page, order, category)
        self.search_url = q.url
        return Torrents(q.html_source)
        
def run():
    q = Query('avengers endgame 1080p')
    print(q.url)
    t = Torrents(q.webpage)
    torrent = t.getBestTorrent()
    print(torrent.magnetlink)