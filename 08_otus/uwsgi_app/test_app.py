import http.client
import json


class App:
    def __init__(self):
        self.handlers = {}

    def __call__(self, environ, start_response):
        url = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        if not url.endswith('/'):
            handler = App.no_trailing_slash_handler
        else:
            if url in self.handlers:
                allowed_methods, handler = self.handlers[url]
                if method not in allowed_methods:
                    handler = App.not_allowed_handler
            else:
                handler = App.not_found_handler

        status_code, extra_headers, response_content = handler(environ)
        content_type = 'text/plain'
        if not type(response_content) is str:
            response_content = json.dumps(response_content)
            content_type = 'text/json'

        headers = {
            'Content-Type': content_type
        }
        headers.update(extra_headers)
        start_response('%s %s' % (status_code, http.client.responses[status_code]),
                       list(headers.items()),
                       )
        return [response_content.encode('utf-8')]

    def add_handler(self, url, methods=None):
        methods = methods or ['GET']

        def wrapper(handler):
            self.handlers[url] = methods, handler
        return wrapper

    @staticmethod
    def not_found_handler(environ):
        response_content = 'Not found'
        return 404, {}, response_content

    @staticmethod
    def not_allowed_handler(environ):
        response_content = 'Not allowed'
        return 405, {}, response_content

    @staticmethod
    def no_trailing_slash_handler(environ):
        response_content = 'Redirect to url with trailing slash'
        return 301, {'Location': '%s/' % environ['PATH_INFO']}, response_content


application = App()


@application.add_handler('/', methods=['GET', 'POST'])
def index_page_handler(environ):
    return 200, {}, 'Index'


@application.add_handler('/info/')
def info_page_handler(environ):
    return 200, {}, {'user_ip': environ['REMOTE_ADDR']}
