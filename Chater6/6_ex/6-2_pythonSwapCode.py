# 0 인덱스와 1 인덱스의 원소 교체하기
# 파이썬은 스와프시, 별도 저장용 변수를 사용하지 않아도 된다.

array = [3,5]

array[0], array[1] = array[1], array[0]

print(array)