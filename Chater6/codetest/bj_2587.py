# 백준 2587 : 대표값 2
import sys

array = []
sum = 0
for i in range(5):
    array.append(int(sys.stdin.readline()))
    sum += array[i]
array.sort()

avg = int(sum / len(array))
mid = array[int(len(array)/2)]

print(avg)
print(mid)