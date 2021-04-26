# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 07:24:40 2021

@author: saduq.rahman
"""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def exchange_first_last(seq):
    first = seq[-1:]
    mid = seq[1:-1]
    last = seq[:1]
    return print(first + mid + last)


exchange_first_last(data)


def every_other_removed(seq):
    return print(seq[::2])


every_other_removed(data)


def first4_last4_every_other_removed(seq):

    return print(seq[1:-1:2])


first4_last4_every_other_removed(data)


def seq_reversed(seq):
    return print(seq[::-1])


seq_reversed(data)


def last_third_first_third_mid_third(seq):
    first = seq[-4:]
    mid = seq[6:10]
    last = seq[:4]
    return print(first + last + mid)


last_third_first_third_mid_third(data)
