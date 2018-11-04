#!/usr/bin/env python3

import asyncio
import argparse

import websockets

from .common import forward


def handler(url, t, s):
    async def f(*rw):
        try:
            async with websockets.connect(url) as ws:
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

    eloop = asyncio.get_event_loop()
    h = handler(args.connect, args.buffer_time, args.buffer_size)
    eloop.run_until_complete(asyncio.start_server(h, lhost, lport))
    eloop.run_forever()


if __name__ == '__main__':
    main()
