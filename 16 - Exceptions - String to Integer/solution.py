#!/bin/python3

import math
import os
import random
import re
import sys


S = input()
try:
    integer = int(S)
    print(integer)
except ValueError:
    print('Bad String')
