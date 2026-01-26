#!/usr/bin/env python3
"""
Simple mock LLM server for testing baish ask builtin.

Usage:
    python3 mock-llm-server.py [port]

Returns mock responses in OpenAI-compatible format.
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class MockLLMHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

    def do_GET(self):
        """Handle GET requests (for /models preflight check)"""
        if self.path == '/models' or self.path == '/v1/models':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'object': 'list',
                'data': [
                    {'id': 'test-model', 'object': 'model'},
                    {'id': 'mock-model', 'object': 'model'}
                ]
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """Handle POST requests (for chat completions)"""
        if '/chat/completions' in self.path or '/completions' in self.path:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            try:
                request_data = json.loads(body)
                prompt = request_data.get('input', [{}])[1].get('content', '')

                # Generate mock response based on prompt
                if 'list files' in prompt.lower():
                    answer = "To list files by size, use: ls -lhS"
                    commands = ["ls -lhS"]
                elif 'disk usage' in prompt.lower():
                    answer = "Show disk usage with du command"
                    commands = ["du -sh *"]
                else:
                    answer = f"Mock response to: {prompt[:50]}..."
                    commands = []

                response = {
                    'id': 'mock-response',
                    'object': 'chat.completion',
                    'model': request_data.get('model', 'test-model'),
                    'choices': [{
                        'message': {
                            'role': 'assistant',
                            'content': json.dumps({
                                'answer': answer,
                                'commands': commands
                            })
                        }
                    }]
                }

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MockLLMHandler)
    print(f'Mock LLM server running on http://localhost:{port}')
    print('Press Ctrl+C to stop')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        httpd.shutdown()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
