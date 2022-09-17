from __future__ import annotations

import os
import threading
import warnings

from flask import Flask
from flask import request

from .add_user import add
from .globals import globals as g
from .helpers import restart_ftp_server

warnings.filterwarnings('ignore')

app = Flask(__name__)


def thread_function_add_user():  # username, password):
    # g.ftp_server.authorizer.add_user(username, password, os.path.join(g.ftp_server.files_dir, username), perm='elradfmw')
    g.ftp_server.handler = g.ftp_server.initialize_handler()
    g.ftp_server.authorizer = g.ftp_server.handler.authorizer


@app.route('/add_user', methods=['GET'])
def add_user():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    if username is None or password is None:
        return 'Username or password is missing'

    g.logger.debug(f'Add ftp user: {username} {password}')
    add(username, password)

    # , args=(username, password))
    thread_add_user = threading.Thread(target=thread_function_add_user)
    thread_add_user.start()
    return 'User added successfully', 200


@app.route('/test', methods=['GET'])
def test():
    return 'Test', 200


def start():
    thread_start_ftp_server = threading.Thread(target=restart_ftp_server)
    thread_start_ftp_server.start()

    app.run(host=os.environ.get('FLASK_SERVER_HOST'),
            port=os.environ.get('FLASK_SERVER_PORT'), debug=False)
