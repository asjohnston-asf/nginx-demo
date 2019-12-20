import jwt
from http.cookies import SimpleCookie

PUBLIC_KEY = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDBU3T16Db/88XQ2MTHgm9uFALjSJAMSejmVL+tO0ILzHw2OosKlVb38urmIGQ+xMPXTs1AQQYpJ/CdO7TaJ51pv4iz+zF0DYeUhPczsBEQYisLMZUwedPm9QLoKu8dkt4EzMiatQimBmzDvxxRkAIDehYh468phR6zPqIDizbgAjD4qgTd+oSA9mDPBZ/oG1sVc7TcoP93FbO9u1frzhjf0LS1H7YReVP4XsUTpCN0FsxDAMfLpOYZylChkFQeay7n9CIK8em4W4JL/T0PC218jXpF7W2p92rfAQztiWlFJc66tt45SXAVtD1rMEdWGlzze4acjMn4P7mugHHb17igtlF82H/wpdm84qTPShvBp/F4YZejgAzOAxzKVbCQ8lrApk1XYVDRAVk3AphfvNK5IC/X9zDSXstH9U94z8BTjkL2fR4eKzFu5kkvVoGHAACIv72QvH06Vwd0PNzLyaNXr9D5jO61EbR4RfpbzvAG0IzgXsUq0Rj7qwvzTCu6yLwTi/fn9bmRaOQNPtBch4ai5w7cfUWe2r7ZPv31AXPm1A+aGXvYTEZkiQMrBN/dXlNdUmafNNDoMBm/frQhMl+2DZp+C9GXCr2Z/JmYUHO8PaEj6UyYTkkrmtZNlZ43Nd2TblPEzL0pprJM9MxEf2Peaai8GKmTJz6C5tSGU+XdZQ== root@9dce6b43747e'

def application(env, start_response):
    if 'HTTP_COOKIE' not in env:
        start_response('401 Unauthorized', [])
        return([])

    cookies = SimpleCookie(env['HTTP_COOKIE'])
    if 'asf-urs' not in cookies:
        start_response('401 Unauthorized', [])
        return([])

    token = cookies['asf-urs'].value
    try:
        payload = jwt.decode(token, PUBLIC_KEY)
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        start_response('401 Unauthorized', [])
        return([])

    start_response('200 OK', [('Content-Type','text/html')])
    return [payload['urs-user-id'].encode()]