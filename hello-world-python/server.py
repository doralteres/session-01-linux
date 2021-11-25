import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello roy')


httpd = socketserver.TCPServer(('', 8000), Handler)
print("Example app listening at http://localhost:8000")
httpd.serve_forever()

