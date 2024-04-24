def solution(want, number, discount):
    '''
    XYZ 일정 금액 지불 시 10일 동안 회원 자격 부여
    매일 한 가지 제품을 할인
    자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치하는 경우 회원가입
    
    제한사항
    want -> 1 ~ 10
    number -> 1 ~ 10(number 원소의 합 10)
    discount -> 10 ~ 10만
    
    풀이과정
    want 값은 무조건 10에 수렴
    discount 조건에서 want 조건에 만족하는 경우의 수 찾으면 될 듯
    Count 함수 써서 일치 여부 확인
    '''
    from collections import Counter
    join_dict = {k:v for k, v in zip(want, number)}
    
    answer = 0
    for day in range(len(discount)):
        discount_items = Counter(discount[day:day+10])
        if discount_items == join_dict:
            answer += 1
    return answer

want=["banana", "apple", "rice", "pork", "pot"]
number=[3, 2, 2, 2, 1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

solution(want, number, discount)