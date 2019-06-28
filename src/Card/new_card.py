# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$


class Card(object):
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit, 1, 10)


class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)
