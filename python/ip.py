from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> hello,Kinney</h1>'


@app.route('/login', methods=['post'])
def login():
    print(request.form.items())
    username = request.form.get('username', '')
    return '<h1> hello,%s!</h1>' % username


@app.route('/loginget', methods=['get'])
def loginget():
    for k, v in request.args.items():
        print(k + ':' + v)
    username = request.args.get('username', '')
    return '<h1> hello,%s!</h1>' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0')
