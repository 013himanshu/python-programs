#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    s = list(s)
    result = ""
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
            result = result + s[i]
        elif s[i] == " ":
            s[i+1] = s[i+1].upper()
            result = result + s[i]
        else:
            result = result + s[i]
    return result

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
