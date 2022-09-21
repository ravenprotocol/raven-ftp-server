from __future__ import annotations

import os
from dotenv import load_dotenv
load_dotenv()

FILES_DIR = os.environ.get('FILES_DIR')
USERS_FILE_PATH = os.environ.get('USERS_FILE_PATH')
USER_TABLE_FILE_PATH = os.environ.get('USER_TABLE_FILE_PATH')
RAVFTP_LOG_FILE = os.environ.get('RAVFTP_LOG_FILE')

MASQUERADE_ADDRESS = os.environ.get('MASQUERADE_ADDRESS')
PASSIVE_PORTS = range(60000, 65535)
