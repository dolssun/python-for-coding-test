# 백준 11650 : 좌표 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    x,y = list(map(int, input().split()))
    array.append((x,y))

#print(array)

array.sort(key= lambda x : (x[0], x[1]))
#print(array)
for i in array:
    print(*i)