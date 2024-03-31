import math

'''
주어진 수가 1이 될 때까지 다음 작업 반복
입력된 수가 짝수 -> 2로 나눔
입력된 수가 홀수 -> 3곱하고 1 더함

6이라는 숫자가 주어졌을 때
6/2=3 -> 3*3+1=10 -> 10/2=5 -> 5*3+1=16 -> 16/2=8 -> 8/2=4 -> 4/2=2 -> 2/2=1

포인트는 2의 n승의 경우 결국에는 1로 수렴
2의 n의 구조까지만 하고 나머지는 계산을 하고 브레이크 걸면 되는 구조
단 500번 초과 시 -1이므로 이 점에 유의
'''
num = 32

answer = 0
while True:
    if (num & (num - 1)) == 0 and answer+(int(math.log2(num)))<=500:
        answer += int(math.log2(num))
        break
    if answer <= 500:
        if num%2 == 0:
            num = int(num/2)
            answer += 1
        elif num%2 == 1:
            num = num*3+1
            answer += 1  
    elif answer > 500:
        answer = -1
        break
        
    if num == 1:
        break

print(answer)