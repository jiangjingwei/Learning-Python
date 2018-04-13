import sys
import os
from wsgiref.simple_server import make_server

import re

from views import index
from urls import routes


def post_data(environ):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))

    except ValueError:
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)

    return request_body


def application(environ, start_response):


    # 获取post数据
    request_body = post_data(environ)

    request = {
        "path": environ['PATH_INFO'],
        "data": request_body,
        'query_string': environ['QUERY_STRING'],
    }

    urlpatterns = routes()

    func = None

    for item in urlpatterns:

        pattern = re.compile(item[0])
        if pattern.match(request.get('path')):
            # print(pattern.match(path).group())
            func = item[1]
            break

    if func:
        if request.get('path').endswith('.html'):
            start_response("200 ok", [("Content-Type", "text/html")])
        # elif request.get('path').endswith('v=3.2.1'):
        #     start_response("304 Not Modified")

        elif request.get('path').startswith('/webchat'):
            start_response("200 ok", [("Content-Type", "application/x-www-form-urlencoded")])

        elif request.get('path').endswith('.png'):
            start_response("200 ok", [("Content-Type", "image/png")])
        elif request.get('path').endswith('.gif'):
            start_response("200 ok", [("Content-Type", "image/gif")])
        elif request.get('path').endswith('.jpg'):
            start_response("200 ok", [("Content-Type", "image/jpg")])
        elif request.get('path').endswith('.css'):
            start_response("200 ok", [("Content-Type", "text/css")])
        elif request.get('path').endswith('.js'):
            start_response("200 ok", [("Content-Type", "application/x-javascript")])
        elif request.get('path').startswith('/login'):
            start_response("200 ok", [("Content-Type", "application/x-www-form-urlencoded")])
        elif request.get('path').endswith('v=3.2.1'):
            start_response("200 ok")

        return func(request)

    else:
        return [b"<h1>404 NOT FOUND</h1>"]


if __name__ == "__main__":
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASEDIR)

    server = make_server("", 9999, application)
    print('server starting...')
    server.serve_forever()
