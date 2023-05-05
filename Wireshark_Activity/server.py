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
from urllib import parse
import ssl
import os

# Uncomment if you need to create a new key
#os.system('cmd /k "openssl req -new -x509 -keyout server.pem -out ./key/server.pem -days 365 -nodes"')

def mask(word):
    masked_word = ""
    count = 0
    while(count < len(word)):
        masked_word += '*'
        count = count + 1
    return masked_word

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Need to update this post method ***
    def do_POST(self):
        if self.path == '/submit':
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            uname = ""
            pword = ""
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message = fields.get('message')[0].decode()
                
            else:
                content_length = int(self.headers['Content-Length'])
                message = self.rfile.read(content_length).decode()
                split_msg = str(message).partition("&")
                uname = split_msg[0].partition("=")[2]
                pword = split_msg[2].partition("=")[2]

            print(f"message: {message}")
            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header('Content-type','text/html')
            self.end_headers()

            # Send message back to client
            output = "<!DOCTYPE html>"
            output += "<html lang=\"en\">"
            output += "<head>"
            output += "<meta charset=\"UTF-8\">"
            output += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
            output += "<link rel=\"stylesheet\" href=\"./css/style.css\">"
            output += "<link rel=\"icon\" type=\"image/x-icon\" href=\"/images/WT_logo.ico\">"
            output += "<title>Login Page</title>"
            output += "</head>"
            output += "<body>"
            output += f"<p>Username: {parse.unquote(uname)} <br>"
            output += f"Password: {mask(parse.unquote(pword))} <br>"
            output += "</p></body></html>"

            print(f"INFORMATION:\nUsername:\t{parse.unquote(uname)}\nPassword:\t{parse.unquote(pword)}\n")
            self.wfile.write(bytes(output, "utf-8"))
            return


IP = '10.22.27.113' # Change this to current IP Address
PORT = 8000
Handler = ServerHandler
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