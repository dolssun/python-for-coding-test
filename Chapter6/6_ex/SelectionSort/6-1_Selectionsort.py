array = [7,5,9,0,3,1,6,2,4,8]
#print(array)

for i in range(len(array)):                 # 배열의 길이만큼 for문을 돌릴때 > len() 사용
    min = array[i]
    for j in range(i+1, len(array)):        # n번째 부터 m번째까지 for문 돌릴때 > range(n, m) 으로 표현

        if(array[j] < min):
            min = array[j]
            array[j], array[i] = array[i], min

print(array)