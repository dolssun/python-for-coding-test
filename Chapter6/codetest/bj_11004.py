# 백준 11004 : k 번째 수
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

array = list(map(int, input().split()))
array.sort()

print(array[k-1])