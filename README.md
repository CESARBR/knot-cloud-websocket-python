# KNoT Cloud WebSocket library for Python

A client side library that provides a WebSocket abstraction to KNoT Cloud for Python applications.

## Quickstart

### Install

```
pip install git+https://github.com/CESARBR/knot-cloud-websocket-python@master
```

### Run

Import the library and others dependencies:

```python
import asyncio
from knot_cloud_websocket import create_connection
```

Connect to a KNoT Cloud instance from a coroutine:

```python
async def main():
    async with create_connection(
                hostname='ws.knot.cloud',
                protocol='wss',
                port=443,
                credential_id='e9662e36-e99b-4508-80f9-168a3bbddf7a',
                credential_token='a4ed4893fd591a23f65d32ba7922afc170c0cfa9'
        ) as client:
        pass
```

Add this coroutine to an event loop:

```python
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(handler())
    asyncio.get_event_loop().run_forever()
```

Run your code:

```
python main.py
```

## Development

### Requirements

- make
- Python &gt;= 3.7
- [Poetry](https://poetry.eustace.io)

### Install dependencies

```
poetry install
```

### Test

```
make test
```

### Lint

```
make lint
```

### Documentation

First, update documentation with the docstrings:

```
make api-doc
```

Then, generate HTML documentation:

```
cd docs
make html
```