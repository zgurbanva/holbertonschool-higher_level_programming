#!/usr/bin/python3
"""
Module: task_03_http_server
Description: Implements a simple HTTP server using Python’s http.server module.
Handles multiple endpoints and returns text or JSON responses accordingly.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler."""

    def do_GET(self):
        """Handle GET requests with different endpoints."""
        # Root endpoint: simple text response
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint: return JSON
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpoint: API status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))

        # /info endpoint (optional, from example output)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Undefined endpoint: return 404 error
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Run the HTTP server on port 8000."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:8000 ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
