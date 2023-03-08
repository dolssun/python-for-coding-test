# 백준 10814 : 나이순 정렬

import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    age, name = list(map(str, sys.stdin.readline().split()))
    array.append((int(age), name))

array.sort(key = lambda x : x[0])
for i in array:
    print(i[0], i[1])
