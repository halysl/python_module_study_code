# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

import random
from new_generate_card import card5


class Deck(list):
    def __init__(self, decks=1):
        super().__init__()
        for _ in range(decks):
            self.extend(card5(r+1, s)
                        for r in range(13)
                        for s in ('Club', 'Diamond', 'Heart', 'Spade'))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for _ in range(burn):
            self.pop()
