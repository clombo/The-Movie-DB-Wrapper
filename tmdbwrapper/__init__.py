#tmdbwrapper/__init__.py

import os
import requests

TMDB_API_KEY = os.environ.get('TMDB_API_KEY',None)

#API endpoints
LINKS = {
    "info":"https://api.themoviedb.org/3/tv/{}",
    "popular":"https://api.themoviedb.org/3/tv/popular"
    }

class APIKeyMissingError(Exception):
    pass

if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "No API key found. Please make sure to add a API key to your environment variables. "
        "See documentation for more information on https://github.com/clombo/The-Movie-DB-Wrapper/blob/master/README.md"
    )


session = requests.Session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY

from tv import TV
