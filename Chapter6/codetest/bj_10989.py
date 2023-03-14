# 백준 10989 : 수 정렬하기 3

import sys
input = sys.stdin.readline

n = int(input())
array = [0]*10000

# 방법 1
# for i in range(n):
#     array.append(int(input()))
#
# #print(array)
# array.sort()
# #print(array)
#
# for i in array:
#     print(i)

# 방법 2 : 계수 정렬 이용하기

for i in range(n):
    input_data = int(input())
    array[input_data-1] += 1

for i in range(10000):
    if array[i] != 0:
        for j in range(array[i]):
            #print('( ' + str(i) + ', ' + str( j+1) + ')', end=' ')
            print(i+1)