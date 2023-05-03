"""

File:   server.py
Author: Nickolas Gallegos
Date:   1 May 2023
Desc:   This file runs a simple http server.
Info:   https://docs.python.org/3/library/http.server.html

"""


import http.server
import socketserver
import logging
import cgi
import ssl
import os

# Uncomment if you need to create a new key
#os.system('cmd /k "openssl req -new -x509 -keyout server.pem -out ./key/server.pem -days 365 -nodes"')

# Potentially need to update this entire class ***
class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Need to update this post method ***
    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        with open("data.txt", "w") as file:
            for key in form.keys(): 
                file.write(str(form.getvalue(str(key))) + ",")

IP = '192.168.1.106' # Change this to current IP Address
PORT = 8000
Handler = ServerHandler
with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    # The code below will "wrap" the socket to use TLS 1.3
    #httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./key/server.pem', server_side=True)
    print("serving at port", PORT)
    httpd.serve_forever()