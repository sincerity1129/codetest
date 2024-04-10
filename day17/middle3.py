def solution(a, b, n):
    '''
    콜라 빈병 20개 -> 콜라 10병
    콜라 빈병 10개 -> 콜라 5병
    콜라 빈병 4개 -> 콜라 2병
    콜라 빈병 2개 -> 콜라 1병
    콜라 빈병 2개 -> 콜라 1병
    10+5+2+1+1 = 19병
    
    풀이 과정
    개수를 계속 a로 나눠 떨어지는 경우랑 아닌 경우 나눠서 생각
    개수 카운팅 해서 콜라 1병이거나 0병일 때까지 진행
    '''
    answer = 0
    while True:
        if n % a == 0:
            answer += b*(n // a)
            n = b*(n // a)
        else:
            answer += b*(n // a)
            n = b*(n // a) + n % a
        if n < a:
            break
    return answer

a=3
b=1
n=20
solution(a, b, n)