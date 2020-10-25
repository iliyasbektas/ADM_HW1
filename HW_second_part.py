#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Recursive Digit Sum

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    return 1 + (k * sum(int(x) for x in n) - 1) % 9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


# viral advertising
n = int(input())
shared = 5
total_liked = 0

for i in range(0, n):
    liked = int(shared // 2)
    total_liked = total_liked + liked
    shared = liked * 3
    
print(total_liked)


# In[ ]:


# Number line jumps

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 == x2): 
        return 'YES'
    elif (x1 > x2):
        return 'NO'
    elif (v2 > v1):
        return 'NO'
    elif (v2 == v1):
        return 'NO'
    x1 += v1;
    x2 += v2;
    return (kangaroo(x1, v1, x2, v2))


# fptr = open(os.environ['OUTPUT_PATH'], 'w')

x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
result = kangaroo(x1, v1, x2, v2)
print(result)

# fptr.write(result + '\n')
# fptr.close()


# In[ ]:


# birthday cake candles
n_candles = input()
candles_height  = list(map(int, input().split()))
tallest_candles = max(candles_height)
print (candles_height.count(tallest_candles))

