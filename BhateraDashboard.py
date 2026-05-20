#!/usr/bin/env python3
"""
BhateraDashboard.py
Serves the Bhatera dashboard (index.html / style.css / app.js)
from the parent directory and opens it in the browser.
"""
import http.server
import socketserver
import webbrowser
import os
import sys
import threading

# Resolve the dashboard directory
SCRIPT_DIR    = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# Verify required files are present
REQUIRED = ["index.html", "style.css", "app.js"]
missing  = [f for f in REQUIRED if not os.path.isfile(os.path.join(DASHBOARD_DIR, f))]
if missing:
    print(f"[BHATERA] ERROR — missing files in {DASHBOARD_DIR}:")
    for f in missing:
        print(f"          * {f}")
    sys.exit(1)

# Custom handler
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DASHBOARD_DIR, **kwargs)
    def log_message(self, fmt, *args):
        code = args[1] if len(args) > 1 else ""
        if str(code).startswith(("4", "5")):
            super().log_message(fmt, *args)

# Open browser after a short delay
def open_browser():
    url = f"http://localhost:{PORT}"
    print(f"[BHATERA] Dashboard -> {url}")
    webbrowser.open(url)

timer = threading.Timer(0.6, open_browser)
timer.daemon = True
timer.start()

# Start server
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    print(f"[BHATERA] Serving from  {DASHBOARD_DIR}")
    print(f"[BHATERA] Port          {PORT}")
    print(f"[BHATERA] Press Ctrl+C to stop\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[BHATERA] Server stopped.")
