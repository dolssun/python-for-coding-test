# 백준1181 : 단어 정렬
n = int(input())
#array = list(map(str, input().split()))
array = []

for i in range(n):
    array.append(str(input()))

set_array = set(array)   # set 형식을 통해 중복제거
array = list(set_array)  # list 형태로 다시 변환

array.sort()
array.sort(key=len)

for i in array:
    print(i)