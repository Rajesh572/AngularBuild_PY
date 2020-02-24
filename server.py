import http.server
import socketserver


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if (
            self.path == "/"
            or self.path == "/dashboard"
            or self.path == "/reports/select"
        ):
            self.path = "index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 9012
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
try:
    my_server.serve_forever()
except KeyboardInterrupt:
    my_server.server_close()
