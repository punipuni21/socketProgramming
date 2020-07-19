import http.server

PORT = 8080

handlerclass = http.server.SimpleHTTPRequestHandler
simpled = http.server.HTTPServer(("", PORT), handlerclass)
simpled.serve_forever()