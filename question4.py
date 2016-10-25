#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
扑克牌
@author: zhengxiaoyao0716
"""


from util import read_inputs, StrValidator


CARDS = {str(i): i for i in range(3, 11)}
CARDS.update({
    "J": 11, "Q": 12, "K": 13, "A": 14, "2": 15,
    "joker": 16, "JOKER": 17
})


def compare_cards(left, right):
    """比较两手牌"""
    if left[1] == 0:
        return left[0]
    if right[1] == 0:
        return right[0]
    if left[1] == 4:
        if right[1] == 4:
            return left[0] if left[0][0] > right[0][0] else right[0]
        return left[0]
    if right[1] == 4:
        return right[0]
    if left[1] != right[1]:
        return 'ERROR'
    # if left[1] == 5:
    #     return left[0] if left[0][4] > right[0][4] else right[0]
    return left[0] if left[0][0] > right[0][0] else right[0]


def cards_from_group(input_str):
    """解析输入"""
    cards = input_str.split()
    length = len(cards)
    if length > 5:
        return None
    link_count = 0
    last_card = cards[0]
    for index in range(0, length):
        card = cards[index]
        if card not in CARDS:
            return None
        diff = CARDS[card] - CARDS[last_card]
        if diff == 1:
            link_count += 1
            last_card = card
        elif diff != 0:
            return None
    if link_count == 0 or link_count == 4:
        return (cards, length)
    if length == 2:
        return (cards, 0) if cards[0] == 'joker' else None


def main():
    """Entrypoint"""
    while True:
        group0, group1 = read_inputs(
            '请输入两手牌，两手牌中间用“-”连接，' +
            '每手牌的每张牌以空格分隔，“-”两边没有空格，' +
            '如：4 4 4 4-joker JOKER）\n',
            StrValidator(), StrValidator(),
            separate='-'
        )
        left = cards_from_group(group0)
        if not left:
            print('第一手牌不合法：', group0)
            continue
        right = cards_from_group(group1)
        if not right:
            print('第二手牌不合法：', group0)
            continue
        print(compare_cards(left, right))
        if read_inputs('输入"Y"继续，否则退出', StrValidator()).upper() != 'Y':
            break
if __name__ == '__main__':
    main()
