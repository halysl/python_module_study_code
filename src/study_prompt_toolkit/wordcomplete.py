# -*- coding: utf-8 -*-

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.python import Python3Lexer


def main():
    history = InMemoryHistory()
    our_style = Style.from_dict(
        {
            'pygments.comment': '#888888 bold',
            'pygments.keyword': '#ff88ff bold'
        }
    )
    python_completer = WordCompleter(['import', 'self', '[]', 'set', 'list'])

    while True:
        text = prompt(
            '> ',
            lexer=PygmentsLexer(Python3Lexer),
            history=history,
            completer=python_completer,
            style=our_style)
        if text in ["exit", "quit"]:
            break
        print('You entered:', text)
    print('GoodBye!')

if __name__ == "__main__":
    main()
