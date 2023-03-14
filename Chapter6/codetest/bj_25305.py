# 백준 25305 : 커트라인

import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

array = list(map(int, input().split()))
#print(array)

array.sort(reverse=True)
#print(array)

print(array[k-1])