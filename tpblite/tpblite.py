from .models.torrents import Torrents, Torrent
from .models.utils import Query

class TPB(object):
    
    def __init__(self, base_url='https://tpb.party'):
        self.base_url = base_url
        
    def search(self, query, base_url, page=0, order=99, category=0):
        webpage = Query(query, base_url, page=0, order=99, category=0)
        return Torrents(webpage)
        
def run():
    q = Query('avengers endgame 1080p')
    print(q.url)
    t = Torrents(q.webpage)
    torrent = t.getBestTorrent()
    print(torrent.magnetlink)