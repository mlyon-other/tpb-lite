Unofficial Lightweight Python API for ThePirateBay

Installation
=============
```sh
$ pip install tpblite
```

Dependencies:
 - BeautifulSoup
 - purl

Usage
==========

```python
from tpblite import TPB

# Create a TPB object with a domain name
t = TPB('https://thepiratebay.org')

# Or create a TPB object with default domain
t = TPB()
```
## Search
```python
# Quick search for torrents, returns a Torrents object
torrents = t.search('public domain')

# See how many torrents were found
print('There were {0} torrents found.'.format(len(torrents))

# Iterate through list of torrents and print info for Torrent object
for torrent in torrents:
    print(torrent)

# Customize your search
from tpblite import CATEGORIES, ORDERS
torrents = t.search('public domain', page=2, order=ORDERS.NAME.DEC, category=CATEGORIES.VIDEO.MOVIES)

# Get the most seeded torrent based on a filter
torrent = torrents.getBestTorrent(min_seeds=30, min_filesize='500 MiB', max_filesize='4 GiB')

# Or select a particular torrent by indexing
torrent = torrents[3]

# Get the magnet link for a torrent
print(torrent.magnetlink)
```
## Browse
```python
# You can browse all of the torrents from a single category
torrents = t.browse(category=CATEGORIES.VIDEOS)
# Customize the page number and sort order
torrents = t.browse(category=CATEGORIES.VIDEO.MOVIES, page=1, order=ORDERS.UPLOADED.DES)
```

## Categories and Sort Order
```python
# To print all available categories, use the classmethod printOptions
CATEGORIES.printOptions()
# Or just a subset of categories, like VIDEOS
CATEGORIES.VIDEO.printOptions()
# Similarly for the sort order
ORDERS.printOptions()
```

## Torrents object
The search function returns a `Torrents` object, which is a *list-like* collection of the torrents found.

You can also iterate over the `Torrents` object just by calling it in a for loop (see example above).

You can see how many `Torrent` objects your query has returned, by using the `len()` function

## Torrent object
`Torrent` objects represent each torrent found in the `Torrents` class, they have the following attributes
### Attributes
- `Torrent.title` - The name of the torrent (str)
- `Torrent.seeds` - The number of seeders (int)
- `Torrent.leeches` - The number of leechers (int)
- `Torrent.upload_date` - Date the torrent was uploaded (str)
- `Torrent.uploader` - Name of user who uploaded torrent (str)
- `Torrent.filesize` - The filesize in *iB format, eg. 5 GiB (str)
- `Torrent.byte_size` - The filesize in bytes of the torrent (int)
- `Torrent.magnetlink` - magnetlink of the torrent (str)


Example Workflow
==========

With a commandline torrent client such as [aria2](https://aria2.github.io/), you can automate search and downloading of torrents like so:
```python
import subprocess
from tpblite import TPB

t = TPB()
torrents = t.search('GIMP 2.10.8')
torrent = torrents.getBestTorrent()
subprocess.call(['aria2c', torrent.magnetlink])
```
