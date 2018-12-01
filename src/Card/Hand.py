# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

class Hand(object):
    def __init__(self, delealer_card):
        self.delealer_card = delealer_card
        self.cards = []
    
    def hard_total(self):
        return sum(c.hard for c in self.cards)
    
    def soft_total(self):
        return sum(c.soft for c in self.cards)