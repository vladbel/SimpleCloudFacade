#
# server.py
# functionality for facade servers
#

import http.server

class FacadeRequestHandler(http.server.BaseHTTPRequestHandler):
    """Request handler for the cloud facade HTTP server"""

    def do_GET(self):
        """HTTP GET handler"""

        self.wfile.write(bytes("<html><body>This is a test</body></html>", "UTF-8"))
        self.send_response(200)


def serve(port):
    server_address = ("", port)
    httpd = http.server.HTTPServer(server_address, FacadeRequestHandler)
    httpd.serve_forever()
    