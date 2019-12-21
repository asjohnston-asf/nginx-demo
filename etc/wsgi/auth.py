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

    user_id = payload[env['JWT_USER_FIELD']]
    header = ('user_id', user_id)

    if 'JWT_GROUP_NAME' in env and 'JWT_APP_UID' in env:
        found = False
        for group in payload.get('urs-groups', []):
            if group.get('name') == env['JWT_GROUP_NAME'] and group.get('app_uid') == env['JWT_APP_UID']:
                found = True
        if not found:
            start_response('403 Forbidden', [header])
            return([])

    start_response('200 OK', [header])
    return([])