from enum import Enum

ROUTES = {'/': 'index',
          '/login': 'login',
          '/account': 'account'}


TEMPLATES_DIR = 'templates/'


class HttpStatusCode(Enum):
    OK = '200 OK'
    NOT_FOUND = '404 Not Found'
