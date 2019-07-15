# -*- coding: utf-8 -*-
from urllib import request, parse


def get_request():
    url = 'http://httpbin.org/get'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    querystring = parse.urlencode(parms)

    get_request = request.urlopen(url+'?' + querystring)
    resp = get_request.read()
    print(resp)


def post_request():
    url = 'http://httpbin.org/post'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    querystring = parse.urlencode(parms)
    post_request = request.urlopen(url, querystring.encode('ascii'))
    resp = post_request.read()
    print(resp)


def add_header():
    url = 'http://httpbin.org/get'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }

    req = request.Request(url, querystring.encode('ascii'), headers=headers)

    # Make a request and read the response
    u = request.urlopen(req)
    resp = u.read()
    print(resp)

if __name__ == "__main__":
    get_request()
    post_request()
