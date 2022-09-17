from __future__ import annotations

import json
from _md5 import md5
from argparse import ArgumentParser

from .config import USERS_FILE_PATH
from .globals import globals as g


def add(username, password):
    users = None
    g.logger.debug(f'Inside add:{USERS_FILE_PATH}')
    with open(USERS_FILE_PATH) as openfile:
        details = json.load(openfile)
        users = details['users']

    g.logger.debug(f'users:{str(users)}')

    user = [user['username'] for user in users if user['username'] == username]

    # Check user
    if len(user) == 0:
        # Do not add user
        password = md5(password.encode('latin1')).hexdigest()

        users.append({
            'username': username,
            'password': password,
        })

        details['users'] = users

        with open(USERS_FILE_PATH, 'w') as f:
            json.dump(details, f)

        g.logger.debug(
            '{}'.format({
                'username': username,
                'password': password,
            }),
        )
    else:
        password = md5(password.encode('latin1')).hexdigest()

        users2 = []
        for index, user1 in enumerate(users):
            if user1['username'] == username:
                users2.append({
                    'username': username,
                    'password': password,
                })
            else:
                users2.append(user1)

        details['users'] = users2

        with open(USERS_FILE_PATH, 'w') as f:
            json.dump(details, f)

        g.logger.debug(
            '{}'.format({
                'username': username,
                'password': password,
            }),
        )


if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('--username', type=str,
                           default=None, help='Enter username')
    argparser.add_argument('--password', type=str,
                           default=None, help='Enter password')

    args = argparser.parse_args()

    add(args.username, args.password)
