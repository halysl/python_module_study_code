# -*- coding: utf-8 -*-

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.python import Python3Lexer


def main():
    history = InMemoryHistory()

    while True:
        text = prompt('> ', lexer=PygmentsLexer(Python3Lexer), history=history)
        if text in ["exit", "quit"]:
            break
        print('You entered:', text)
    print('GoodBye!')

if __name__ == "__main__":
    main()
