# 백준11399 - ATM

n = int(input())
array = list(map(int, input().split()))

array.sort()
sum = 0

for i in range(n):
    for j in range(0,i+1,1):
        #print(array[j], end=' ')
        sum += array[j]

print(sum)





