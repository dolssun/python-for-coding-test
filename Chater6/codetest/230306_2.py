# 백준11399 - ATM

n = int(input())
array = list(map(int, input().split()))

array.sort()
total = 0

#for i in range(n):
 #   for j in range(0,i+1,1):
  #      #print(array[j], end=' ')
   #     sum += array[j]

for i in range(1, n+1):
    total += sum(array[0:i])
print(total)





