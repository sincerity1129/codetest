# answer = 0

def solution(storey):
    # global answer
    '''
    마법의 엘리베이터 -> -1, +1, -10, +10, -100, +100
    엘리베이터는 0보다 작으면 움직이지 않음(0층이 가장 아래층)
    
    storey = 층수
    최소한의 방법을 통해 0층으로 가기 위한 방법 찾기
    
    stroey = 16 (1~1억)
    두가지 방법
    1. -1 -> 6번 -10 -> 1번 // 7번
    2. 1 -> 4번 -10 -> 2번 // 6번
    
    stroey = 2554
    -1 -> 4번, +10 -> 5번, +100 -> 4번, -1000 -> 3번 // 16번
    
    풀이 과정
    위로 올라갈 지 내려갈 지 정하고 움직이면 되는 문제로 보임
    5일 때 다음이 5이상이면 올라가는 게 좋고 5미만이면 내려가는 게 좋지만 마지막은 내려가는 게 좋음
    마지막 값은 무조건 내려가야함
    다만 1억까지의 숫자를 가지고 있으므로 재귀함수를 활용해서 계속 쓰면 좋아 보임


    다른 풀이 과정
    
    '''
    # storey = str(storey)
    # now_floor = int(storey[-1])
    
    # if len(storey) == 1:
    #     answer += now_floor
    #     return answer
    # if now_floor > 5:
    #     answer += 10-now_floor
    #     if storey[-2] == '9':
    #         storey = storey[:-2] + '0' + storey[-1]
    #         solution(storey[:-1])
    #     else:
    #         storey = storey[:-2] + str(int(storey[-2])+1) + storey[-1]
    #         solution(storey[:-1])
    # elif now_floor == 5:
    #     if len(storey) == 2 or int(storey[-3]) < 5:
    #         answer += now_floor
    #         solution(storey[:-1])
    #     elif int(storey[-3]) >= 5:
    #         answer += 10-now_floor
    #         if storey[-2] == '9':
    #             storey = storey[:-2] + '0' + storey[-1]
    #             solution(storey[:-1])
    #         else:
    #             storey = storey[:-2] + str(int(storey[-2])+1) + storey[-1]
    #             solution(storey[:-1])
                
    # elif now_floor == 0:
    #     solution(storey[:-1])
    # else:
    #     answer += now_floor
    #     solution(storey[:-1])
    answer = 0
    while True:
        remainder = storey % 10
        if len(str(storey)) == 1:
            answer += remainder
            break
        if remainder > 5:
            answer += 10-remainder
            storey += 10
        elif remainder < 5:
            answer += remainder
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
                answer += remainder
            else:
                answer += 10-remainder
                
        storey //= 10
    return answer


storey=75021
answer = solution(storey)
print(answer)
'''
75021
-1 -> 1 / -2 -> 2 / 0 -> 0 / 5 -> 5 / 8 -> 8 
-1 -> 1 / -2 -> 2 / 0 -> 0 / 5 -> 5 / 8 -> 8
'''