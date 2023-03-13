# 백준 11931 : 수 정렬하기 4

import sys
input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]
# for i in range(n):
#     array.append(int(input()))

#print(array)

array.sort(reverse=True)
#print(array)

for i in array:
    print(i)