# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from card import NumberCard, AceCard, FaceCard


def card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception('Rank out of index!')


def card2(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    else:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)


def card3(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard('K', suit)
    else:
        raise Exception('Rank out of index')


def card4(rank, suit):
    class_ = {1: AceCard, 11: FaceCard,
              12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_
