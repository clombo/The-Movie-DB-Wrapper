#tmdbwrapper/apibase.py


"""
Base data of TMDB API including API base URL, endpoints, version and other URL data
Also creates a session in which calls can be made

"""

import os
import requests
from .error import *

#API base url
API_BASE_URL = "https://api.themoviedb.org"

#API version
API_VERSION = "3"

#API_endpoints
API_ENDPOINTS = { "account":"account","tv":"/tv/","movie":"/movie/"}

#API Key received from env variable
TMDB_API_KEY = os.environ.get('TMDB_API_KEY',None)



class apiBase(object):

    def __init__(self):
        self.baseurl = self._SetBase()
        self.session = self._CreateSession()

    def _SetBase(self):
        return "{}/{}/".format(API_BASE_URL,API_VERSION)

    def _CreateSession(self):

        if TMDB_API_KEY is None:
            raise APIKeyMissingError(
                "No API key found. Please make sure to add a API key to your environment variables. "
                "See documentation for more information on https://github.com/clombo/The-Movie-DB-Wrapper/blob/master/README.md"
            )
        
        session = requests.Session()
        session.params = {}
        session.params['api_key'] = TMDB_API_KEY

        return session

