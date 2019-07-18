# -*- coding: utf-8 -*-
# 利用闭包特性

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

if __name__ == "__main__":
    base_url = "https://www.google.com/search?q={search}"
    yahoo = UrlTemplate(base_url)
    for line in yahoo.open(search='ces'):
        print(line.decode('utf-8'))

    yahoo = urltemplate(base_url)
    for line in yahoo(search="qwer"):
        print(line.decode('utf-8'))
