# 백준 18870 : 좌표 압축
import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

print(array)

sorted_list = sorted(list(set(array)))
print(sorted_list)

dic = {sorted_list[i]:i for i in range(len(sorted_list))}
print(dic)
for i in array:
    print(dic[i], end=' ')


