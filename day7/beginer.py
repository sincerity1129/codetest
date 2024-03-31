p = "3141592"
t = "271"

# 숫자로 이루어진 문자열 t, p
# t에서 p와 길이가 같은 부분문자 중에서 p가 나타내는 수보다 작거나 같은 것 횟수 구하기
# p의 길이는 1~18
# t는 p~1만
# 0으로 시작하지 않음

# t = "3141592", P="271"
# p의 길이 3이고 t -> 314, 141, 159, 592
# p 271보다 작거나 같은 경우는 141, 159

# 풀이과정
# 슬라이싱 해서 값을 가져오는 방식
# 중간에 0으로 시작하는 경우 이를 숫자로 표현 필요

slicing_numbers = [t[i:i+len(p)] for i in range(0, len(t)-(len(p)-1), 1)]
answer = sum(1 for number in slicing_numbers if int(number)<=int(p))