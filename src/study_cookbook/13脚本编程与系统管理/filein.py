# -*- coding: utf-8 -*-

import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(f_input.filename(), f_input.lineno(), line, end='')
