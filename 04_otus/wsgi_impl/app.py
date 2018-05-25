from config import ROUTES, HttpStatusCode
import utils


def application(environ, start_response):
    path = environ['PATH_INFO']
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    page_name = ROUTES.get(path, None)

    if page_name:
        status = HttpStatusCode.OK.value
        content = utils.get_content(page_name)
    else:
        status = HttpStatusCode.NOT_FOUND.value
        content = b'Error occurred'
    start_response(status, headers)
    return [content]