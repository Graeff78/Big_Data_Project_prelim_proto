class movie:
    """ contains all the attributes of a movie """
    def __init__(self, item):
        self.id = item["id"]
        self.genre_ids = item["genre_ids"]
        self.title = item["title"]
        self.original = item["original_title"]
        self.overview = item["overview"]
        self.voteavg = item["vote_average"]
        self.votecnt = item["vote_count"]
        self.pop = item["popularity"]
        self.date = item["release_date"]
        self.lang = item["original_language"]
        self.adult = item["adult"]
        self.poster = item["poster_path"]
        self.backdrop = item["backdrop_path"]

#help(movie)