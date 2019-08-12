# -*- coding: utf-8 -*-
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise

example()
