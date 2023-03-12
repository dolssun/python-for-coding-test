# 백준 10867 : 중복빼고 정렬하기
import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
array = list(set(array))                    # set은 중복허용 x
array.sort()

print(*array)

#print(*list(set(array)))