import http.client


class App:

    def __call__(self, environ, start_response):

        url = environ['PATH_INFO']
        handlers = {
            '/info/': info_page_handler,
            '/': index_page_handler
        }
        if url in handlers:
            handler = handlers[url]
        else:
            handler = not_found_handler

        status_code, extra_headers, response_content = handler(environ)
        headers = {
            'Content-Type': 'text/plain'
        }
        headers.update(extra_headers)
        start_response('%s %s' % (status_code, http.client.responses[status_code]),
                       list(headers.items()),
                       )
        return [response_content]


application = App()


def info_page_handler(environ):
    response_content = b'Hello world from a simple WSGI application'
    return 200, {}, response_content


def index_page_handler(environ):
    response_content = b'Index'
    return 200, {}, response_content


def not_found_handler(environ):
    response_content = b'Not found'
    return 404, {}, response_content