from __future__ import annotations
from ravftp.helpers import stop_server, start_server, restart_ftp_server

from argparse import ArgumentParser

from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('--action', type=str,
                           default=None, help='Enter action')

    args = argparser.parse_args()

    if args.action == 'stop':
        stop_server()
    elif args.action == 'start':
        start_server()
    elif args.action == 'restart':
        restart_ftp_server()
