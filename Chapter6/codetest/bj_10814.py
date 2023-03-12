# 백준 10814 : 나이순 정렬

n = int(input())
array = []

for i in range(n):
   #input_data = input().split()
   age, name = list(map(str, input().split()))
   age = int(age)
   array.append((age,name))
   #array.append((input_data[0],input_data[1]))

print(array)
array.sort(key= lambda x: x[0])

for i in array:
    print(i[0], i[1])