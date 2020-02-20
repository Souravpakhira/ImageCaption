from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello world!"


@app.route('/hi')
def Hi():
    return "Hello sourav"


if __name__ == '__main__':
    app.debug = True
    app.run( port=5000)
