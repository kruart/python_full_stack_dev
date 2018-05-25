import config
import utils


def application(environ, start_response):
    path = environ['PATH_INFO']
    headers = [('Content-Type', 'text/html')]

    page_name = config.ROUTES.get(path, None)

    if page_name:
        status = config.HttpStatusCode.OK.value
        content = utils.get_content(page_name)
    else:
        status = config.HttpStatusCode.NOT_FOUND.value
        content = b'Error occurred'
    start_response(status, headers)
    return [content]