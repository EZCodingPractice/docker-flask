from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'KEEP LEARNING, KEEP MOVING AHEAD - NEVER STOP'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
