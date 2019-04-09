# KNoT Cloud WebSocket library for Python

A client side library that provides a WebSocket abstraction to KNoT Cloud for Python applications.

## Quickstart

### Install

```
pip install git+https://github.com/CESARBR/knot-cloud-websocket-python@master
```

### Run

Import the library:

```python
import knot_cloud_websocket
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