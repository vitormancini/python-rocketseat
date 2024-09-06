from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client has been disconnected to the server')

@socketio.on('message')
def message(message):
    socketio.emit('message', message)


if __name__ == '__main__':
    socketio.run(app, debug=True)