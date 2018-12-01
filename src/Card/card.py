# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 21点游戏 https://baike.baidu.com/item/21%E7%82%B9/5481683


class Card(object):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.soft, self.hard = self._point()
    
    def _point(self):
        return 0, 0

class NumberCard(Card):
    def _point(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _point(self):
        return 1, 11

class FaceCard(Card):
    def _point(self):
        return 10, 10


        