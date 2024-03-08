#!/bin/python3

import math
import os
import random
import re
import sys

def max_consecutive_ones(n):
    temp = 0
    res = 0
    while n != 0:
        if n % 2 == 1:
            temp += 1
        else:
            temp = 0
        res = max(temp, res)
        n //= 2
    return res

if __name__ == '__main__':
    n = int(input().strip())
    print(max_consecutive_ones(n))
