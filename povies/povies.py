import requests

class Povies:
    """
    This class provides methods for movie requests
    """
    def __init__(self):
        pass


    def movies(self, limit):
        """
        - List some movies 
        - Requires a limit
        - Movies are:
            * sorted by seeds.
            * ordered n ascending order
            * quality of 1080p
        - Returns 50 movies at max with a default of 20
        """
        url = 'https://yts.ag/api/v2/list_movies.json?sort=seeds&limit=%s&order_by=asc&quality=1080p' % limit
        res = requests.get(url)
        dic = res.json()
        return dic["data"]["movies"]

    
    def search(self, query):
        """
        - Search for movies 
        - Requires a search query
        - Movies are:
            * sorted by highest number of downloads.
            * quality of 1080p
        """
        url = 'https://yts.ag/api/v2/list_movies.json?query_term=%s&sort_by=download_count&quality=1080p' % query
        res = requests.get(url)
        dic = res.json()
        return dic["data"]["movies"]


    def movie(self, movie_id):
        """
        - Fetch a movie detail
        - Requires a movie_id
        """
        url = 'https://yts.ag/api/v2/movie_details.json?movie_id=%s' % movie_id
        res = requests.get(url)
        dic = res.json()
        return dic["data"]["movie"]


    def related(self, movie_id):
        """
        - Fetch movies related to a movie
        - Requires a movie_id
        """
        url = 'https://yts.ag/api/v2/movie_suggestions.json?movie_id=%s' % movie_id
        res = requests.get(url)
        dic = res.json()
        return dic["data"]["movies"]