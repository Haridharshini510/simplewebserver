from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<body>
<h1>HARIDHARSHINI (24900163)</h1>
<ol>
<li>Device name	HARIDHARSHINI</li>
<li>Processor	13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
<li>Installed RAM	16.0 GB (15.7 GB usable)</li>
<li>Device ID	9A4CCD7D-7150-41B6-9FF6-5362C24C5E5A</li>
<li>Product ID	00342-42691-71307-AAOEM</li>
<li>System type	64-bit operating system, x64-based processor</li>
<li>Pen and touch	No pen or touch input is available for this display</li>
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()