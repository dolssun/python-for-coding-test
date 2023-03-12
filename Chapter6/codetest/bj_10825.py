# 백준 10825 : 국영수
import sys
input = sys.stdin.readline
n = int(input())

array = []
for i in range(n):
    #input_data = input().split()
    name, k,e,m = list(map(str, input().split()))
    # k = int(k)
    # e = int(e)
    # m = int(m)
    array.append([name, int(k), int(e), int(m)])

# <정렬 방법1> 직접 정렬시, 정렬 1순위를 가장 마지막으로 정렬해주어야 한다.
# array.sort(key=lambda x: x[0])
# array.sort(key=lambda x: x[3], reverse=True)
# array.sort(key= lambda x: x[2])
# array.sort(key= lambda x: x[1],reverse=True)

# <정렬 방법2> lambda를 사용하여 정렬 조건을 걸어준다
array.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))
for i in array:
    print(i[0])