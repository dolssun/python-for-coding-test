# 백준_1427 : 소트인사이드

array = list(map(int, input()))

#print(*array)      // 괄호없이 출력하는 방법

array.sort(reverse=True)
for i in range(len(array)):
    print(array[i], end='')         # 띄어쓰기 없이 한번에 출력방법