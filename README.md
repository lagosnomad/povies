# Povies v1 - Python wrapper

## Description

Python 2 library for [YTS](https://tys.ag).
It provides *search, listing and  data retrieval* API's for integration purposes.

## Python version

Library built and tested on *python2*.

## How to install

Package is available with [PyPI](https://pypi.python.org/pypi)

You can use pip for the installation

```bash
pip install -U povies
```

## Functions and methods

All the callable methods are using the [YTS REST API](https://yts.ag/api)

## Usage

See the examples/example.py file

```python
# Get movies with a limit
print p.movies(10)

# Get a movie using the movie_id
print p.movie(1)

# # Get movies related to a movie using the movie_id
print p.related(1)

# Search for a movie
print p.search("ninja")

# Download a movie torrent using the movie_id
print p.download(23) # This uses your default torrent application to donwload the movie
```
