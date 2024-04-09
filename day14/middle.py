from itertools import combinations
def solution(numbers):
    '''
    numbers -> 정수 배열
    서로 다른 인덱스 2개 뽑아 만들 수 있는 배열 return
    
    풀이
    combinations 모듈 쓰면 쉽게 해결 될 듯
    '''
    comb_list = combinations(numbers, 2)
    answer = [a+b for a, b in comb_list]
    return sorted(set(answer))

numbers = [2,1,3,4,1] 
solution(numbers)
