def solution(left, right):
    '''
    두 정수 left, right
    left ~ right(1 <= left <=  right <= 1000)
    약수의 개수가 짝수는 더하고 약수의 개수가 홀수는 뺀 수
    
    예시 
    left=13, right=17
    13에서 17까지의 약수 구해서 값 구하기 
    13 -> 2, 14 -> 4, 15 -> 4, 16 -> 5, 17 -> 2
    
    풀이과정
    약수 구하는 함수로 개수 구하고 홀수 - 짝수 +
    '''
    
    def find_divisors(n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        divisors_count = len(divisors)
        if divisors_count % 2 ==0:
            return 1
        return -1
    
    answer = 0
    for num in range(left, right+1):
        answer += num*find_divisors(num)
        
    return answer


left=13
right=17

solution(left, right)