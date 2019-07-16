# -*- coding: utf-8 -*-
import requests

UNKNOWN = "Unknown"


def request_header():
    resp = requests.head('http://www.python.org/index.html')
    status_code = resp.status_code
    server = resp.headers.get("Server", UNKNOWN)
    location = resp.headers.get("Location", UNKNOWN)
    content_length = resp.headers.get('Content-Length', UNKNOWN)
    print(f"status code:{status_code}, content_length: {content_length} "
          f"server: {server}, location: {location}")


def cookie_transfer():
    # First request
    url = "http://www.python.org/index.html"
    resp1 = requests.get(url)

    # Second requests with cookies received on first requests
    resp2 = requests.get(url, cookies=resp1.cookies)


def upload_file():
    url = 'http://httpbin.org/post'
    files = {'file': ('data.csv', open('data.csv', 'rb'))}

    r = requests.post(url, files=files)


def test_on_httpbin():
    """
    >>> import requests
    >>> r = requests.get('http://httpbin.org/get?name=Dave&n=37',
    ...     headers = { 'User-agent': 'goaway/1.0' })
    >>> resp = r.json
    >>> resp['headers']
    {'User-Agent': 'goaway/1.0', 'Content-Length': '', 'Content-Type': '',
    'Accept-Encoding': 'gzip, deflate, compress', 'Connection':
    'keep-alive', 'Host': 'httpbin.org', 'Accept': '*/*'}
    >>> resp['args']
    {'name': 'Dave', 'n': '37'}
    >>>
    """
    pass

if __name__ == "__main__":
    request_header()
