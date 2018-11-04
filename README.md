# Websocket Port Mapping

# Requirements

Python 3.5+

# Install

1. Clone the repository

    ```sh
    git clone https://github.com/gaohuazuo/wspm.git
    cd wspm
    ```

1. (Optional) Create a virtualenv and activate

    ```sh
    virtualenv pyenv --python=python3
    . pyenv/bin/activate
    ```

2. Install with `pip`

    ```sh
    pip install -e .
    ```

# Example

On server side, suppose you want to expose the ssh port (22) to clients,

```sh
python3 -m wspm.server :80 localhost:22
```

On client side,

```sh
python3 -m wspm.client localhost:2222 ws://example.com:80
```

Now the port mapping has been set up. Test it with

```sh
ssh -p 2222 username@localhost -v
```

# WSS

Although `wss` protocol is not supported natively, you can enable `wss` with a CDN like Cloudflare.

# Note

This is a minimal prototype. Do not use it unless you understand what it is doing.

Feel free to submit an issue or pull request!
