#!/usr/bin/env python3

import asyncio
import argparse

import websockets

from common import forward


def handler(host, port, t, s):
    async def f(ws, uri):
        rw = await asyncio.open_connection(host, port)
        try:
            await forward(ws, rw, t, s)
        finally:
            rw[1].close()
    return f


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('listen', type=str)
    parser.add_argument('connect', type=str)
    parser.add_argument('--buffer-time', '-t',
                        type=float, default=50)
    parser.add_argument('--buffer-size', '-s',
                        type=int, default=1024)
    args = parser.parse_args()

    try:
        lport = int(args.listen)
        lhost = 'localhost'
    except ValueError:
        lhost, lport = args.listen.split(':')
        lport = int(lport)
    try:
        cport = int(args.connect)
        chost = 'localhost'
    except ValueError:
        chost, cport = args.connect.split(':')
        cport = int(cport)

    eloop = asyncio.get_event_loop()
    h = handler(chost, cport, args.buffer_time, args.buffer_size)
    eloop.run_until_complete(websockets.serve(h, lhost, lport))
    eloop.run_forever()


if __name__ == '__main__':
    main()
