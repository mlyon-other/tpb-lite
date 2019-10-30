from .models.torrents import Torrents, Torrent
from .models.utils import Query



def run():
    q = Query('avengers endgame 1080p')
    print(q.url)
    t = Torrents(q.webpage)
    torrent = t.getBestTorrent()
    print(torrent.magnetlink)