# -*- coding: utf-8 -*-


def format_number():
    x = 1234.56789
    
    # Two decimal places of accuracy
    print(format(x, '0.2f'))

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))

    # Left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))

if __name__ == "__main__":
    format_number()
