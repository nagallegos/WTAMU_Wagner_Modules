"""

File:   server.py
Author: Nickolas Gallegos
Date:   1 May 2023
Desc:   This file runs a simple http server.
Info:   https://docs.python.org/3/library/http.server.html

"""


from http.server import CGIHTTPRequestHandler
import socketserver
import ssl

# Uncomment if you need to create a new key
#os.system('cmd /k "openssl req -new -x509 -keyout server.pem -out ./key/server.pem -days 365 -nodes"')

IP = '172.20.10.9' # Change this to current IP Address
PORT = 8000
Handler = CGIHTTPRequestHandler
document_root = './'

with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    # The code below will "wrap" the socket to use TLS
    #httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./key/server.pem', server_side=True)
    try:
        httpd.document_root = document_root
        print(f'Starting server on {IP}:{PORT}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Stopping server...')