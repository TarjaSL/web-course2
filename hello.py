def wsgi_application(environ, start_response):
status = '200 OK'
headers = [
('Content-Type', 'text/plain')
]
S = environ['QUERY_STRING']
n = S.rfind('?') + 1	
body = S[n:len(S)]
body = body.replace('&', '\n')
start_response(status, headers )
return [ body ]
