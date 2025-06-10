import http.server
import socketserver
import os
from functools import partial

from . import generate_code_structure

PORT = 8000
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SCRIPT_DIR, **kwargs)
    
    def end_headers(self):
        # Add no-cache headers before ending headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        # Override to ensure we never return 304
        # Remove conditional headers that would trigger 304 responses
        if 'If-Modified-Since' in self.headers:
            del self.headers['If-Modified-Since']
        if 'If-None-Match' in self.headers:
            del self.headers['If-None-Match']
        
        # Call parent's do_GET which will now always return 200
        super().do_GET()

if __name__ == "__main__":
    generate_code_structure.main()

    # Serve files from the script directory with no caching
    print(f"Serving `explore_code` on http://localhost:{PORT} (no caching)")
    with ReusableTCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        httpd.serve_forever()