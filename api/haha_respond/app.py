'''
__author__ = 'TAOG'
author_email='wenter.wu#gamil'
'''

from flask import Flask

app = Flask(__name__)


@app.route("/ping")
def index():
    '''
    PING API
    :return: pong
    '''
    return "pong"

