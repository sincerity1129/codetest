def solution(a, b):
    '''
    요일을 맞추는 문제
    
    풀이과정
    월별로 리스트 만들어서 월별 계산
    그 달의 경우에는 b의 값을 더해서 7로 나눈 나머지를 요일로 표기
    1월 1일 기준으로 1%7하면 1이 기준 값
    그러므로 0은 목요일
    '''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    return week[(sum(month[:(a-1)]) + b) % 7]

a=1
b=1
answer = solution(a, b)

print(answer)