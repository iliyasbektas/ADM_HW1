#!/usr/bin/env python
# coding: utf-8

# In[ ]:



my_string = "Hello, World!"
print(my_string)


# In[ ]:




import math
import os
import random
import re
import sys

n = int(raw_input().strip())

if n % 2 != 0:
   print("Weird")
else:
     if  2 <= n <=5:
        print("Not Weird")
     elif 6 <= n  <=20:
        print("Weird")
     elif n>=20:
        print("Not Weird")


# In[ ]:



if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)


# In[ ]:



if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a//b)
print (a/b)


# In[ ]:


if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i*i)


# In[ ]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 100 == 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    elif year % 4 == 0:
        leap = True
    
    return leap


# In[ ]:


if __name__ == '__main__':
    n = int(input())

for i in range(1, n+1):
    print(i, end='')


# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

a = [[l,m,k] for l in range(x+1) for m in range(y+1) for k in range(z+1) if l+m+k != n]
print(a)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


arr = set(arr)
arr = sorted(list(arr)) # runner up score
print(arr[-2])


# In[ ]:


n=int(input())
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])    
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x]) # the second lowest grade


# In[ ]:


if __name__ == '__main__':
    
    res = {}
    n = int(input())
    for _ in range(n):
        name, *line = input().split()
        marks = list(map(float, line))
        res[name] = marks
    name = input()
    score= res[name]
    b=(sum(score)/len(score))
    print (b)


# In[ ]:


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


# In[ ]:


import re
TESTER = re.compile(
    r"^"
    r"\d{3}"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")


# In[ ]:


def swap_case(s):
    return s.swapcase()


# In[ ]:


def print_full_name(a, b):
    print("Hello", a, b + "! You just delved into python.")


# In[ ]:


def mutate_string(string, position, character):
    
    return string[:position] + character + string[position+1:]


# In[ ]:


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    
    return count


# In[ ]:


if __name__ == '__main__':
    s = str(input())
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))
    


# In[ ]:


def split_and_join(line):
    T = line.split(" ")
    return "-".join(T)


# In[ ]:


N,M= map(int,input().split())
pattern = [ ((".|.")*(2*i+1)).center(M,'-') for i in range(N//2) ]

print('\n'.join( pattern + ["WELCOME".center(M,'-')] + pattern[::-1] ))


# In[ ]:


def print_formatted(num):

    w = len("{0:b}".format(num))

    for n in range(1, num + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(n, w = w))




# In[ ]:


import textwrap
import string
import sys


def remove_duplicates_in_str(arg_str):
    new_str = ''
    len_str = len(arg_str)
    for ch in arg_str:
        if ch in new_str:
            continue
        else:
            new_str += ch

    return new_str




def merge_the_tools(string, k):
 
    len_of_u_string = int(k)
    len_of_full_string = len(string)
    u_tmp = []
    i = 0
    for i in range(0,len(string),int(k)):
        tmp_str = string[i:i+len_of_u_string]
        tmp_str = remove_duplicates_in_str(tmp_str)
        print(tmp_str)
        u_tmp.append(tmp_str)

    return 0


# In[ ]:


def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])


# In[ ]:


number_of_countries = int(input())
set_of_countries = set(input() for i in range(number_of_countries))
    
print (len(set_of_countries))


# In[ ]:



num1 = int(input())
set1 = set(map(int, input().split()))
num2 = int(input())
set2 = set(map(int, input().split()))
u = set1.union(set2)

print (len(u))


# In[ ]:


num1 = int(input())
set1 = set(map(int, input().split()))
num2 = int(input())
set2 = set(map(int, input().split()))
i = set1.intersection(set2)

print (len(i))


# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n_shoes = int(input())
list_shoe_sizes = list(map(int, input().split())) 
dictionary_for_shoe_sizes = Counter(list_shoe_sizes)
set1 = []
n_customers = int(input()) 

for i in range(n_customers):
    s, p = map(int, input().split())
    
    if s in dictionary_for_shoe_sizes and dictionary_for_shoe_sizes[s] > 0:
        set1.append(p)
        dictionary_for_shoe_sizes[s] -= 1
print(sum(set1))


# In[ ]:


import calendar

date = list(map(int,input().split()))
a = calendar.weekday(date[2],date[0],date[1])
week = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

print (week[a])


# In[ ]:


# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

n_stud, n_sub = map(int, input().split())

courses = list()

for n in range(0, n_sub):
    courses.append(list(map(float, input().split())))

pupils = list(zip(*courses))

for n in range(0, n_stud):
    scores = 0
    for j in range(0, n_sub):
        scores += pupils[n][j]
    print (scores / n_sub)


# In[ ]:


string = input()

def f(x):  # we have functions for everything except even functions 
    if x.isdigit():
        if int(x)%2 ==0:
            return True
        else: return False
    else: return True

print (*sorted(string,key = lambda i:(i.isdigit(),f(i),i.isupper(),i)),sep='') 


# In[ ]:


def fibonacci(n):
    list1 = []
    for i in range(n) :
        if i <= 1 :
                list1.append(i)
        else:
                f = int(list1[i-2])+int(list1[i-1])
                list1.append(f)
    return list1
def cube(n):
    return (n*n*n)

print (list(map(cube,fibonacci(num))))


# In[ ]:


import re

string = input()
regex_pattern = r"[,.]"


print("\n".join(re.split(regex_pattern, string)))


# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
print (next((k for k, l in zip(string, string[1:]) if k == l and k.isalnum()), -1))


# In[ ]:


set1 = set(map(int, input().split()))
num = int(input())
result = True

for i in range(num):
    set2 = set(map(int, input().split()))
    if not set2.issubset(set1):
        result = False
    if len(set2) >= len(set1):
        result = False

print(result)


# In[ ]:


for i in range(int(input())):  
    num1 = int(input())
    set1 = set(map(int, input().split()))
    num2 = int(input())
    set2 = set(map(int, input().split()))
    if set1.issubset(set2) : print (True)
    else : print (False)


# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
num1 = int(input())
set1 = set(map(int, input().split()))
num2 = int(input())
set2 = set(map(int, input().split()))
i = set1.difference(set2)

print (len(i))


# In[ ]:


import numpy as np

set1 = np.array(input().split(' '),int)
set1 = set1.reshape(3,3)
print (set1)


# In[ ]:


import numpy as np 

parameters = list(map(int, input().split()))
array1 = np.array([input().split() for i in range(parameters[1])], int)
array2 = np.array([input().split() for i in range(parameters[0])], int)

print (np.concatenate((array1, array2), axis = 0))


# In[ ]:


import numpy as np 
a = list(map(int,input().split()))

print (np.zeros(a,dtype = np.int))
print (np.ones(a,dtype = np.int))


# In[ ]:


import numpy as np

nm = list(map(int, input().split(' ')))
#print (np.identity(nm[0]))
print (np.eye(nm[0], nm[1], k = 0))


# In[ ]:


import numpy as np
nm = list(map(int,input().split()))
a1,a2 = [],[]
for i in range(nm[0]):
    a1.append(list(map(int,input().split())))
for i in range(nm[0]):
    a2.append(list(map(int,input().split())))
A1,A2 = np.array(a1),np.array(a2)
print (np.add(A1,A2))
print (np.subtract(A1,A2))
print (np.multiply(A1,A2))
print (np.floor_divide(A1,A2))
print (np.mod(A1,A2))
print (np.power(A1,A2))


# In[ ]:



import numpy as np

array = np.array(input().split(), float)
print (np.floor(array))
print (np.ceil(array))
print (np.rint(array))


# In[ ]:


import numpy as np
nm = list(map(int,input().split()))
n = [list(map(int,input().split())) for _ in range(nm[0])]
array = np.array(n)
summation = np.sum(array,axis=0)
print (np.prod(summation,axis=0))


# In[ ]:


import numpy as np
nm = list(map(int,input().split()))
array = np.array([list(map(int,input().split())) for _ in range(nm[0])])
mini = np.min(array,axis=1)
print (np.max(mini))


# In[ ]:


import numpy as np 
nm = list(map(int,input().split()))
n = [list(map(int,input().split())) for _ in range(nm[0])]
array = np.array(n)
print (np.mean(array, axis = 1))
print (np.var(array, axis = 0))
print (np.std(array, axis = None))


# In[ ]:


import numpy as np

n= int(input())
A = np.array([input().split() for i in range(n)], int)
B = np.array([input().split() for i in range(n)], int)
print (np.dot(A, B))


# In[ ]:


import numpy as np

array1 = np.array(input().split(), int)
array2 = np.array(input().split(), int)

print (np.inner(array1, array2))
print (np.outer(array1, array2))


# In[ ]:


import numpy as np

A = list(map(float, input().split()))
print (np.polyval(A, int(input())))


# In[ ]:


import numpy as np

n = int(input())
array = np.array([list(map(float, input().split())) for i in range(n)])
print (np.linalg.det(array))


# In[ ]:


import numpy as np

n = int(input())
array = np.array([list(map(float, input().split())) for i in range(n)])
print (np.linalg.det(array))


# In[ ]:



nm = numpy.array(list(map(float,input().split())))
print nm[::-1]
def arrays(arr):

