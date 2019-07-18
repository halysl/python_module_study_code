# -*- coding: utf-8 -*-

from urllib.request import urlopen
from xml.etree.ElementTree import parse


def example_xml_parse():
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        guid = item.findtext("guid")
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print("title:{}\ndate:{}\nlink:{}\nguid:{}\n".format(
            title, date, link, guid))
        break

if __name__ == "__main__":
    example_xml_parse()
