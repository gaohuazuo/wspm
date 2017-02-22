# Websocket Port Mapping

# Requirements

Python 3.5+ and websockets library, available via `pip install websockets`.

# Example

On both client and server side, clone the repository and cd to it.

```sh
git clone https://github.com/gaohuazuo/wspm
cd wspm
```

On server side, suppose you want to expose `127.0.0.1:1080` to clients,

```sh
./server.py :80 localhost:1080
```

On client side,

```sh
./client.py localhost:1080 ws://yourserver.com
```

# WSS

Although `wss` protocol is not supported natively, you can enable `wss` with a CDN like Cloudflare.

# Note

This is a minimal prototype. Do not use it unless you understand what it is doing.

Feel free to submit an issue or pull request!
