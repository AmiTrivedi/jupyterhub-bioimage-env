#!/bin/bash
ACTION=$1
PORT=$2


SHARED_MODELS="/cloud/wwu1/u_cryptomatortest/share_data/samapi_models/models"

    

if [ "$ACTION" == "start" ]; then
    echo "Starting SAM API..."
    

    #  Create symbolic link from shared models to ~/.samapi
   
    ln -sfn "$SHARED_MODELS" ~/.samapi

    #  Set environment variable (for samapi library)
    export SAMAPI_ROOT_DIR="$SHARED_MODELS"
    # Start SAM API in background
    nohup python3 -m uvicorn samapi.main:app --host 0.0.0.0 --port 8000 > ~/sam_api.log 2>&1 &
    
   
    python3 -c "
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>API server started</h1><p>It may take some time to download all the models. You can see the log in <b>sam_api.log</b> under your home directory. You can close the tab now.</p>')
HTTPServer(('0.0.0.0', $PORT), Handler).serve_forever()
"

elif [ "$ACTION" == "stop" ]; then
    echo "Stopping SAM API..."
    pkill -f 'uvicorn samapi.main:app'
    
    python3 -c "
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>API server stopped</h1><p>You can close the tab now.</p>')
HTTPServer(('0.0.0.0', $PORT), Handler).serve_forever()
"
fi