answer = 0
def solution(numbers, target):
    '''
    n개의 음이 아닌 정수
    순서대로 더하거나 빼서 target의 경우의 수 구하기
    numbers 길이 -> 2 ~ 20
    numbers -> 1 ~ 50
    target -> 1 ~ 1000
    numbers = [1, 1, 1, 1, 1]
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    
    풀이 과정
    4개가 +이고 나머지 1개가 -
    경우의 수 5개
    
    target이 나오는 조합으로 묶고 경우의 수 구하면 될 듯
    '''
    num_sum = 0
    
    def calculation_case(numbers, num_sum, negative=False):
        global answer
        global target
        
        if len(numbers) == 0:
            return 0
        if negative:
            num_sum -= numbers[0]
        else:
            num_sum += numbers[0]
        if len(numbers) == 1 and num_sum == target:
            answer += 1
        calculation_case(numbers[1:], num_sum)
        calculation_case(numbers[1:], num_sum, negative=True)
        return answer
    
    calculation_case(numbers, num_sum)
    numbers[0] = -1*numbers[0]
    calculation_case(numbers, num_sum)
    return answer

target = 3
numbers = [1,1,1,1,1]
solution(numbers, target)
print(answer)