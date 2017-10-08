import requests
class Povies:
    	def __init__(self):
		pass

	def allmovies(self):
		url = 'https://yts.ag/api/v2/list_movies.json'
		res = requests.get(url)
		dic = res.json()
		return dic