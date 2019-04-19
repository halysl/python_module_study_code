# -*- coding: utf-8 -*-

import html


def parse_html():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))
    print(html.escape(s, quote=False))

if __name__ == "__main__":
    parse_html()
