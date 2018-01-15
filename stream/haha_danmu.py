#!/usr/bin/env python
# encoding=utf-8

import hashlib
import hmac
import logging

import os
from flask import Flask
from flask import abort
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import join_room
from flask_socketio import leave_room


class StreamServerConfig(object):
    DEBUG = bool(os.getenv('DEBUG'))
    ROOM_KEY = os.getenv('ROOM_KEY')
    SOCKETIO_CHANNEL = os.getenv('SOCKETIO_CHANNEL', 'haha-stream')
    CORS_MAX_AGE = 86400
    DANMU_ROOM_ID = 88888


app = Flask(__name__)
app.config.from_object(StreamServerConfig)

# socketio = SocketIO(app,
#                     message_queue=StreamServerConfig.REDIS_URL,
#                     channel=StreamServerConfig.SOCKETIO_CHANNEL)
socketio = SocketIO(app)
cors = CORS(app)


def get_rooms():
    return socketio.server.manager.rooms.get('/', {})


def encode_room_id(plain_room_id, timestamp=None):
    if not StreamServerConfig.ROOM_KEY:
        return plain_room_id

    mixed_room_id = '{plain_room_id}.{timestamp}'.format(plain_room_id=plain_room_id,
                                                         timestamp=timestamp)
    signature = hmac.new(StreamServerConfig.ROOM_KEY,
                         mixed_room_id,
                         hashlib.sha1).hexdigest()
    return '{mixed_room_id}.{signature}'.format(mixed_room_id=mixed_room_id,
                                                signature=signature)


def decode_room_id(cipher_room_id):
    if check_room_id(cipher_room_id):
        return cipher_room_id.split('.')[0]


def check_room_id(cipher_room_id):
    if not cipher_room_id:
        return False

    if not StreamServerConfig.ROOM_KEY:
        # always be true
        return True

    if cipher_room_id.count('.') != 2:
        return False

    plain_room_id, timestamp, _ = cipher_room_id.split('.')
    return cipher_room_id == encode_room_id(plain_room_id, timestamp)


@app.route('/danmu', methods=['POST'])
def send_event():
    try:
        request_json = request.get_json(force=True, silent=True)
    except Exception as e:
        logging.error("Parse request error: %s.", e.message)
        return abort(400)

    event = request_json.get('event')
    body = request_json.get('data')
    # room_id = request_json.get('room')
    room_id = StreamServerConfig.DANMU_ROOM_ID

    if not (event and body and room_id):
        logging.error("Parse request failed, arguments is missing.")
        return abort(400)

    # room_id = decode_room_id(room_id)
    if not room_id:
        logging.error("Room id is invalid.")
        return abort(403)

    if room_id not in get_rooms():
        logging.error("Room id not exist.")
        return abort(404)

    socketio.emit(event, body, room=room_id)
    return ''


@socketio.on('enter_room')
def enter_room_event(room_id):
    # room_id = decode_room_id(room_id)
    if not room_id:
        logging.error("Room id is invalid.")
        return

    join_room(room_id)


@socketio.on('leave_room')
def leave_room_event(room_id):
    # room_id = decode_room_id(room_id)
    if not room_id:
        logging.error("Room id is invalid.")
        return

    leave_room(room_id)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3200)
