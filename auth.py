import jwt
from http.cookies import SimpleCookie


def application(env, start_response):
    if 'HTTP_COOKIE' not in env:
        start_response('401 Unauthorized', [])
        return([])

    cookies = SimpleCookie(env['HTTP_COOKIE'])
    if env['JWT_COOKIE_NAME'] not in cookies:
        start_response('401 Unauthorized', [])
        return([])

    token = cookies[env['JWT_COOKIE_NAME']].value
    try:
        payload = jwt.decode(token, env['JWT_PUBLIC_KEY'])
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        start_response('401 Unauthorized', [])
        return([])

    user_id = payload[env['JWT_USER_FIELD']].encode()
    start_response('200 OK', [('Content-Type','text/html')])
    return [user_id]