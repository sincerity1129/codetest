def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


answer = 0
explored = {}
def solution(nums):
    '''
    주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 수
    nums -> 매개변수(3 ~ 50의 길이, 1 ~ 1000 자연수, 중복된 숫자X)
    
    nums=[1,2,3,4]
    1,2,4 -> 7 소수
    
    풀이과정 모든 경우의 수 구함
    sum해서 소수인지 파악
    재귀함수 써서 풀면 쉽게 해결 될 듯
    '''
    
    def decimal_count(nums, decimal_list, depth=1):
        global answer, explored        
        decimal_list.append(nums[0])
        
        try:
            explored[str(decimal_list)]
            return 0
        except:
            if len(decimal_list) == 3:
                explored[str(decimal_list)] = True
                n = sum(decimal_list)
                if len(nums) == 1:
                    decimal_list.remove(decimal_list[1])
                    decimal_list.remove(nums[0])
                else:
                    decimal_list.remove(nums[0])
                if is_prime(n):
                    answer += 1
                return 0
            
        for idx in range(depth, len(nums)):
            decimal_count(nums[idx:], decimal_list)
            
    for idx in range(len(nums)):
        decimal_count(nums[idx:], [])
    return answer


nums = [1,2,7,6,4]
answer = solution(nums)

print(answer)