def app(environ, start_response):
  body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
        
  status = "200 Ok"
  headers = [
      ('Content-type', 'text/plain')
  ]
  start_response(status, headers)
  return body
