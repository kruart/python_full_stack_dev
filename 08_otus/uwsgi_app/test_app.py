import http.client


class App:
    def __init__(self):
        self.handlers = {}

    def __call__(self, environ, start_response):
        url = environ['PATH_INFO']

        if url in self.handlers:
            handler = self.handlers[url]
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
        return [response_content.encode('utf-8')]

    def add_handler(self, url):
        def wrapper(handler):
            self.handlers[url] = handler
        return wrapper


application = App()


@application.add_handler('/')
def index_page_handler(environ):
    response_content = 'Index'
    return 200, {}, response_content


@application.add_handler('/info/')
def info_page_handler(environ):
    response_content = 'Hello world from a simple WSGI application'
    return 200, {}, response_content


def not_found_handler(environ):
    response_content = 'Not found'
    return 404, {}, response_content
