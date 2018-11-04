import asyncio

import websockets


async def tcp2ws(ws, r, t=50, s=1024, max_read=2**20):
    t /= 1000
    buf = bytearray(b'')
    need_flush = asyncio.Event()
    drained = asyncio.Event()
    drained.set()
    timer = None
    should_stop = False

    async def flush():
        nonlocal timer
        while not should_stop or buf:
            await need_flush.wait()
            need_flush.clear()
            data = bytes(buf)
            del buf[:]
            drained.set()
            if timer is not None:
                timer.cancel()
                timer = None
            await ws.send(data)

    async def timer_job():
        nonlocal timer
        await asyncio.sleep(t)
        need_flush.set()
        timer = None

    async def read():
        nonlocal should_stop, timer
        while True:
            await drained.wait()
            data = await r.read(max_read)
            buf.extend(data)
            if not data:
                should_stop = True
                need_flush.set()
                break
            if len(buf) > s:
                drained.clear()
                need_flush.set()
            elif timer is None:
                timer = asyncio.ensure_future(timer_job())

    await asyncio.gather(flush(), read())


async def ws2tcp(ws, w):
    while True:
        data = await ws.recv()
        assert isinstance(data, bytes)
        w.write(data)
        await w.drain()


async def forward(ws, rw, t, s):
    r, w = rw
    await asyncio.gather(tcp2ws(ws, r, t, s), ws2tcp(ws, w))
