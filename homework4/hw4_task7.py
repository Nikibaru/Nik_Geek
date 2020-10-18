from itertools import count
from math import factorial as fr
def fact(n):
    for i in count(1):
        if i <= n:
            yield fr(i)
        else:
            break

n=5
for i in fact(n):
    print(i)
