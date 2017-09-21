#tmdbwrapper/tv.py
from . import *

class TV(object):
    
    def __init__(self,id):
        self.id = id

    def info(self):
        #print LINKS['info'].format(self.id)
        #response = session.get(LINKS['info'].format(self.id))
        path = "https://api.themoviedb.org/3/tv/{}".format(self.id)
        response = session.get(path)
        return response.json()

    @staticmethod
    def popular():
        path = "https://api.themoviedb.org/3/tv/popular"
        response = session.get(path)
        return response.json()
