
class OPTION:
    @classmethod
    def printOptions(cls):
        for opt in [x for x in cls.__dict__.keys() if not (x.startswith('__') or x.startswith('printOptions'))]:
            if hasattr(getattr(cls,opt),'__dict__'):
                for sub_opt in [y for y in getattr(cls,opt).__dict__.keys() if not (y.startswith('__') or y.startswith('printOptions'))]:
                    print('{}.{}'.format(opt,sub_opt))
            else:
                print(opt)

class ORDERS(OPTION):

    class NAME(OPTION):
        DES = 1
        ASC = 2

    class UPLOADED(OPTION):
        DES = 3
        ASC = 4

    class SIZE(OPTION):
        DES = 5
        ASC = 6

    class SEEDERS(OPTION):
        DES = 7
        ASC = 8

    class LEECHERS(OPTION):
        DES = 9
        ASC = 10

    class UPLOADER(OPTION):
        DES = 11
        ASC = 12

    class TYPE(OPTION):
        DES = 13
        ASC = 14


class CATEGORIES(OPTION):
    ALL = 0
      
    class AUDIO(OPTION):
        ALL = 100
        MUSIC = 101
        AUDIO_BOOKS = 102
        SOUND_CLIPS = 103
        FLAC = 104
        OTHER = 199

    class VIDEO(OPTION):
        ALL = 200
        MOVIES = 201
        MOVIES_DVDR = 202
        MUSIC_VIDEOS = 203
        MOVIE_CLIPS = 204
        TV_SHOWS = 205
        HANDHELD = 206
        HD_MOVIES = 207
        HD_TV_SHOWS = 208
        THREE_DIMENSIONS = 209
        OTHER = 299

    class APPLICATIONS(OPTION):
        ALL = 300
        WINDOWS = 301
        MAC = 302
        UNIX = 303
        HANDHELD = 304
        IOS = 305
        ANDROID = 306
        OTHER = 399

    class GAMES(OPTION):
        ALL = 400
        PC = 401
        MAC = 402
        PSX = 403
        XBOX360 = 404
        WII = 405
        HANDHELD = 406
        IOS = 407
        ANDROID = 408
        OTHER = 499

    class PORN(OPTION):
        ALL = 500
        MOVIES = 501
        MOVIES_DVDR = 502
        PICTURES = 503
        GAMES = 504
        HD_MOVIES = 505
        MOVIE_CLIPS = 506
        OTHER = 599

    class OTHER(OPTION):
        EBOOKS = 601
        COMICS = 602
        PICTURES = 603
        COVERS = 604
        PHYSIBLES = 605
        OTHER = 699