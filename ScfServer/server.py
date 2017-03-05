#
# server.py
# functionality for facade servers
#

import http.server
from json.encoder import JSONEncoder
from ScfServer.counter import Counter

request_counter = None

class FacadeRequestHandler(http.server.SimpleHTTPRequestHandler):
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
        global request_counter
        if (request_counter == None):
            request_counter = Counter()
        result = {
            "method":method,
            "path":self.path,
            "value": request_counter.get_value()
        }
        
        encoder = JSONEncoder()
        content = encoder.encode(result)
        self.set_headers()
        self.wfile.write(bytes(content, "UTF-8"))
        


    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=UTF-8')
        self.end_headers()
        


def serve(port):
    server_address = ("", port)
    httpd = http.server.HTTPServer(server_address, FacadeRequestHandler)
    httpd.serve_forever()
    