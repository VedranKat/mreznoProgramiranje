from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host = "localhost"
port = 8000

class webStranica(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Naslov</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Vedran Katavic. 28.04.2020.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webStranica = HTTPServer((host, port), webStranica)  

    try:
        webStranica.serve_forever()
    except KeyboardInterrupt:
        pass
    webStranica.server_close()
    