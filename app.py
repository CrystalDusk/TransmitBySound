import http.server
import ssl
import os

keyfile = r"..\localhost+2-key.pem"
certfile = r"..\localhost+2.pem"
port = 443

httpd = http.server.HTTPServer(('localhost', port), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile, certfile=certfile, server_side=True)
print(f"Serving on https://localhost:{port}")
#os.chdir(r"C:\Users\aaa\Desktop\quiet\quiet-quiet-js-7278254")
httpd.serve_forever()