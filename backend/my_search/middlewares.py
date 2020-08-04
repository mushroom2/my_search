from http import HTTPStatus

from django.http import HttpResponse


__all__ = ['CORSMiddleware']


class CORSMiddleware:
    """
    CORS middleware.
    It was implemented due to the reason that nginx allows adding optional
    headers to responses only when the response code equals 200, 201, 204, 206,
    301, 302, 303, 304, 307, or 308.
    (http://nginx.org/en/docs/http/ngx_http_headers_module.html#add_header)
    Therefore there weren't possible to implement CORS for API using nginx
    facilities only.
    This implementation doesn't match the 'Origin' HTTP header content against
    any list of allowed origins, therefore any origins are allowed.
    """
    AC_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
    AC_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
    AC_MAX_AGE = 'Access-Control-Max-Age'
    AC_ALLOW_METHODS = 'Access-Control-Allow-Methods'
    AC_ALLOW_HEADERS = 'Access-Control-Allow-Headers'

    ALLOWED_METHODS = ', '.join((
        'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
    ))

    ALLOWED_HEADERS = ','.join((
        'Accept',
        'Accept-Encoding',
        'Accept-Language',
        'Authorization',
        'Cache-Control',
        'Connection',
        'Content-Type',
        'DNT',
        'Host',
        'If-Modified-Since',
        'Keep-Alive',
        'Origin',
        'Pragma',
        'Referer',
        'X-CSRFToken',
        'X-Requested-With',
        'User-Agent',
    ))

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_ORIGIN'):
            if all((request.method == 'OPTIONS',
                    'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META)):
                response = HttpResponse(status=HTTPStatus.NO_CONTENT)
                response['Content-Length'] = 0
                response[self.AC_ALLOW_ORIGIN] = \
                    request.META.get('HTTP_ORIGIN')
                response[self.AC_ALLOW_CREDENTIALS] = 'true'
                response[self.AC_MAX_AGE] = 2592000
                response[self.AC_ALLOW_METHODS] = self.ALLOWED_METHODS
                response[self.AC_ALLOW_HEADERS] = self.ALLOWED_HEADERS
                return response

            else:
                response = self.get_response(request)
                origin = request.META.get('HTTP_ORIGIN')
                if origin:
                    response[self.AC_ALLOW_ORIGIN] = origin
                    response[self.AC_ALLOW_CREDENTIALS] = 'true'
                return response

        else:
            return self.get_response(request)