# -*- coding: utf-8 -*-

import os
import textwrap


def parse_long_string():
    s = ("Look into my eyes, look into my eyes, the eyes, the eyes, "
         "the eyes, not around the eyes, don't look around the eyes, "
         "look into my eyes, you're under.")
    print(s)
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent=' '))
    print(textwrap.fill(s, 40, subsequent_indent='***'))


def parse_comfort_info():
    s = ("Beautiful is better than ugly.Explicit is better than "
         "implicit.Simple is better than complex.Complex is better "
         "than complicated.Flat is better than nested.Sparse is "
         "better than dense.Readability counts.Special cases aren't "
         "special enough to break the rules.Although practicality "
         "beats purity.Errors should never pass silently.Unless "
         "explicitly silenced.In the face of ambiguity, refuse the "
         "temptation to guess.There should be one-- and preferably "
         "only one --obvious way to do it.Although that way may not "
         "be obvious at first unless you're Dutch.Now is better than "
         "never.Although never is often better than *right* now.If the "
         "implementation is hard to explain, it's a bad idea.If the "
         "implementation is easy to explain, it may be a good idea."
         "Namespaces are one honking great idea -- let's do more of those!")
    width = os.get_terminal_size().columns
    print(textwrap.fill(s, width))

if __name__ == "__main__":
    parse_long_string()
    parse_comfort_info()
