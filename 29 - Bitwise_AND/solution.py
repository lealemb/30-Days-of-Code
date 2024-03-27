#!/bin/python3
import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    def max_bitwise_and(N, K):
        max_value = 0
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                bitwise_and = i & j
                if max_value < bitwise_and < K:
                    max_value = bitwise_and
                if max_value == K - 1:
                    return max_value
        return max_value

    return max_bitwise_and(N, K)

# Sample input
N = 5
K = 2

print(bitwiseAnd(N, K))

# This part of the code is for HackerRank's input/output handling
# Comment it out if you're testing the function locally
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
