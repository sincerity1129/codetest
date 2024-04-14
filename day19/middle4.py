def solution(k, m, score):
    '''
    사과 상태 -> 1(최하품) ~ K(최상품)
    최하점 받은 사과 -> P, 한 상자의 사과 개수 -> m
    한 상자의 사과 가격 -> p*m
    
    제한 사항
    k -> 3 ~ 9
    m -> 3 ~ 10
    score -> 7 ~ 백만
    사과 한 개 점수 -> 1 ~ k
    이익 없으면 0
    
    예시
    k=3, m=4, score=[1, 2, 3, 1, 2, 3, 1]
    1을 제외한 [2,3,2,3]
    4*2 -> 8
    
    풀이과정
    max 값을 m개 만큼 뽑아 내면 될 듯(시간 초과 이슈)
    
    다른 풀이 과정
    리스트 범위가 3 ~ 9이므로 개수 count해서
    m으로 나눠서 나머지는 아래 수에 더하는 방식으로 진행
    '''
    
    # apple_box = []
    # answer = 0
    # for _ in range(len(score)):
    #     apple_box.append(max(score))
    #     score.remove(max(score))
    #     if len(apple_box) == m:
    #         answer += min(apple_box)*m
    #         apple_box = []
    remain = 0
    answer = 0 
    for quality in range(max(score),min(score)-1,-1):
        answer += (score.count(quality)+ remain) // m * quality * m
        remain = (score.count(quality) + remain) % m
    return answer


# k=3
# m=4
# score=[1, 2, 3, 1, 2, 3, 1]

k=4
m=3
score=[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
answer = solution(k, m, score)

print(answer)