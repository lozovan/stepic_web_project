def app(environ, start_response):
    # Returns a dictionary in which the values are lists

    data = environ['QUERY_STRING']
    d = '\n'.join(str(data).split("&"))

    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [d]