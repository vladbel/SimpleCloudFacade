#
# server.py
# functionality for facade servers
#

import http.server
from json.encoder import JSONEncoder

class FacadeRequestHandler(http.server.BaseHTTPRequestHandler):
    """Request handler for the cloud facade HTTP server"""

    def do_GET(self):
        """HTTP GET handler"""
        self.handle_request("GET")

    def do_POST(self):
        """HTTP POST handler"""
        self.handle_request("POST")

    def do_PUT(self):
        """HTTP PUT handler"""
        self.handle_request("PUT")

    def do_DELETE(self):
        """HTTP DELETE handler"""
        self.handle_request("DELETE")

    def handle_request(self, method):
        result = {
            "method":method,
            "path":self.path
        }
        if "Content-Length" in self.headers:
            result["body"] = self.rfile.read(int(self.headers["Content-Length"])).decode("UTF-8")
        
        encoder = JSONEncoder()
        content = encoder.encode(result)
        self.wfile.write(bytes(content, "UTF-8"))
        self.send_response(200)


def serve(port):
    server_address = ("", port)
    httpd = http.server.HTTPServer(server_address, FacadeRequestHandler)
    httpd.serve_forever()
    