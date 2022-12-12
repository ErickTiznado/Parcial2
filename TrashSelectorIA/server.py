
from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

from PIL import Image



port = 4020



class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        lenc = int(self.headers["Content-Length"])
        data = self.rfile.read(lenc)
        data = data.decode()
        data = parse.unquote(data)


        self.send_response(200)
        self.end_headers()
        self.wfile.write( data.encode() )


server = HTTPServer(("localhost", port), miServidor)
print("Servidor corriendo en el puerto", port)
server.serve_forever()
