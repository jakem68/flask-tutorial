#! /home/jan/flask-tutorial/venv/bin/python3

from flask import Flask, stream_with_context, render_template, request, jsonify, Response
import os, socket, time
from subprocess import call

app = Flask(__name__)

def get_ip():
    ip_address = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip_address = s.getsockname()[0]
        s.close()
    except:
        ip_address = ': Sorry, no network available, so no IP address to show.'
    return ip_address

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print("a = {}, b = {}". format(a, b))
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=('GET', 'POST'))
def hello():
    ip_address = get_ip()
    # ctr=0
    if request.method == 'POST':
        def g():
            counter = int(request.form['counter'])
            for ctr in range(counter):
                time.sleep(1)
                yield str('counting {}'.format(ctr+1))
        return Response(stream_template('hello.html', ip_address=ip_address, data=stream_with_context(g())))
        
    else:
        return render_template('hello.html', ip_address=ip_address)


@app.route('/reboot')
def reboot():
    os.system('sudo reboot -h now')

@app.route('/shutdown')
def shutdown():
    os.system('sudo shutdown -h now')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)