import http.server
import socketserver
import json
import os

PORT = 8000

class DemoRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                "status": "success",
                "message": "Hello from the Python backend!",
                "features": [
                    "Built-in HTTP Server",
                    "Zero External Dependencies",
                    "JSON API Endpoint"
                ]
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        elif self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Demo App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
            text-align: center;
            max-width: 480px;
            width: 90%;
            backdrop-filter: blur(10px);
        }
        h1 {
            color: #1e3c72;
            margin-top: 0;
            font-size: 2.2rem;
            font-weight: 700;
        }
        p {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #555;
            margin-bottom: 2rem;
        }
        .btn {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            border: none;
            padding: 12px 28px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .btn:active {
            transform: translateY(0);
        }
        #api-response {
            margin-top: 2rem;
            padding: 1.2rem;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #2a5298;
            text-align: left;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            white-space: pre-wrap;
            display: none;
            animation: fadeIn 0.5s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Demo App</h1>
        <p>This is a small dummy application showcasing a Python back-end serving static files and API responses.</p>
        <button class="btn" onclick="fetchData()">Fetch API Data</button>
        <div id="api-response"></div>
    </div>

    <script>
        async function fetchData() {
            try {
                const response = await fetch('/api/info');
                const data = await response.json();
                const container = document.getElementById('api-response');
                container.style.display = 'block';
                container.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
    </script>
</body>
</html>
"""
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    # Ensure working directory is set to file directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Starting server at http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), DemoRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
