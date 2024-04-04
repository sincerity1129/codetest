def solution(number, limit, power):
    '''
    각 기사는 1~number 번호가 지정
    자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
    제약사항으로 공격력 제한 수치가 있고 이를 넘는 무기는 정해진 공격력 무기 구해
    
    15번 기사 -> 1,3,5,15 / 4의 공격력
    제약조건이 3이고 공격력 2라면 2의 공격력으로 하락
    
    number = 기사단원의 수
    limit = 공격력 제한 수치(초과 시에만 발동)
    power = 공격력
    
    number = 5
    기사단 = [1,2,3,4,5]
    1 -> 1 / 1
    2 -> 1,2 / 2
    3 -> 1,3 / 2
    4 -> 1,2,4 / 3
    5 -> 1,5 / 2
    1+2*3+3 = 10
    
    풀이 과정
    순차적으로 number를 통해 약수를 구함
    limit 넘어가는 경우 limit의 공격력 더하는 방식하면 결과 도출
    '''
number = 5
limit = 3
power = 2
    
answer = 0

for knight in range(1, number+1):
    tmp = 0
    measure_list = []
    # for idx in range(1, knight+1):
    #     if idx in measure_list:
    #         break
        
    #     if knight%idx == 0 and knight !=1:
    #         if knight/idx == idx:
    #             tmp +=1
    #             continue
    #         tmp +=2
    #         measure_list.append(knight//idx)
    #     elif knight%idx == 0 and knight==1:
    #         tmp +=1
    #     if tmp > limit:
    #         tmp = power
    #         break
    # answer += tmp
    for idx in range(1, int(knight**0.5) + 1):
        if knight % idx == 0:
            tmp += 1
            if idx**2 != knight:               
                tmp += 1
        if tmp > limit:  
            tmp += power            
            break    
    answer += tmp
    
print(answer)