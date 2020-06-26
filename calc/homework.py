from cgi import parse_qs
from homework_template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    str1 = ""
    x = 0
    y = 0
    try:
        a, b = int(a), int(b)
        x = a + b
        y = a * b
    except ValueError:
        if a != '' or b != '':
            str1 = "ValueError"
    response_body = html % {
        'x' : x or 0,
        'y' : y or 0,
        'z' : str1 or "Normal"
        }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]