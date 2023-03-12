#백준 10815 : 숫자 카드
import sys


# 1) for 문 이용하기
input = sys.stdin.readline
n = int(input())

# 집합에 포함되는지 확인할 경우 -> set을 이용하여 중복을 없앤다.
# 시간복잡도 O(n) : 일일히 비교 -> O(1) : set의 시간복잡도
array = set(map(int, input().split()))

m = int(input())
my_list = list(map(int, input().split()))

for i in range(m):
     if my_list[i] in array:
         print(1, end=' ')
     else:
         print(0, end=' ')
