# 백준 5635 : 생일

import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    name, d, m, y = list(map(str, input().split()))
    array.append([name, int(d), int(m), int(y)])

# for i in array:
#     print(i)

array.sort(key= lambda x: (x[3], x[2], x[1]))

# for i in array:
#     print(i)

print(array[n-1][0], array[0][0])