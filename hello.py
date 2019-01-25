#!/usr/bin/env python3
import cgi
import cgitb
import json
import os
from urllib.parse import parse_qs
cgitb.enable() # nice error reporting

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

# Print Query String
qs = os.environ.get("QUERY STRING", None)
print("<dl>")
print("<dt>QUERY STRING</dt>")
print("<dd>{}</dd>".format(parse_qs(qs)))
print("<dt>HTTP_USER_AGENT</dt>")
HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT", None)
print("<dd>" + HTTP_USER_AGENT + "</dd>")
print("</dl>")
# cgi.print_environ()
# print(os.environ)
# json.dumps(os.environ) NO!
print("<pre>")
print(json.dumps(dict(os.environ), indent=4))
print("<pre>")