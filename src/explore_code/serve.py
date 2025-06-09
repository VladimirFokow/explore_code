import http.server
import socketserver
import os
from functools import partial

from . import generate_code_structure

PORT = 8000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    generate_code_structure.main()

    # Serve files from the script directory, regardless of where we launch from
    print(f"Serving explore_code on http://localhost:{PORT}/")
    Handler = partial(http.server.SimpleHTTPRequestHandler, directory=SCRIPT_DIR)
    with ReusableTCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
