#!/usr/bin/python3
"""
    0-making_change
"""


def makeChange(coins, total):
    """
    makeChange:
        args:
            * coins
            * total
        return:
            return the fewest number of coins to meet total
            otherwise -1
    """
    if total < 1:
        return 0

    coins.sort()
    coins.reverse()

    coinDiv = 0
    for coin in coins:
        coinDiv = int(coinDiv + total / coin)
        total %= coin
    if not total:
        return coinDiv
    else:
        return -1
