# Documents for Github pages in this repository

The first function in a code block in markdown

```python
from flask import Flask, stream_with_context, render_template, request, jsonify, Response
import os, socket, time
from subprocess import call, Popen, PIPE

app = Flask(__name__)

def get_ip():
    ip_address = ''
    try:
        cmd="ifconfig | grep '192.168.0'| grep -A 1 '192.168.0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1"
        stdout=Popen(cmd, shell=True, stdout=PIPE).stdout
        ip_address=stdout.read()[:-1].decode("utf-8")

        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8",80))
        # ip_address = s.getsockname()[0]
        # s.close()
    except:
        ip_address = ': Sorry, no network available, so no IP address to show.'
    return ip_address
```

why
