#!/usr/bin/env python3
"""
Simple mock MCP server for testing baish mcp builtin.

Usage:
    python3 mock-mcp-server.py [port]

Responds to /health and /commands endpoints.
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class MockMCPHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status': 'ok', 'version': '1.0'}
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/commands':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            commands = [
                'test_command',
                'echo_command',
                'status_command'
            ]
            self.wfile.write(json.dumps(commands).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

def run_server(port=8081):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MockMCPHandler)
    print(f'Mock MCP server running on http://localhost:{port}')
    print('Press Ctrl+C to stop')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        httpd.shutdown()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8081
    run_server(port)
