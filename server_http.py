import http.server
import socketserver
import webbrowser
import threading

PORT = 7939
URL = f"http://localhost:{PORT}"

Handler = http.server.SimpleHTTPRequestHandler
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
try:
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
except:
    pass
    
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at {URL}")
    
    # Open Edge after 1 second to allow server to start
    threading.Timer(1, lambda: webbrowser.get('edge').open(URL)).start()
    
    # This blocks, so the thread above runs in the background
    httpd.serve_forever()