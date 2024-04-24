def solution(brown, yellow):
    '''
    leo 테두리 1줄은 갈색으로 칠해진 모양 카펫
    brown -> 갈색 격자 수
    yellow -> 노란색 격자 수
    가로 세로 길이 구하는 값
    
    제한 사항
    brown -> 8 ~ 5000
    yellow -> 1 ~ 2백만
    가로 >= 세로
    
    예시
    brown=10, yellow=2
    4*3=12, 10+2
    brown=8, yellow=1
    3*3=9, 8+1
    brown=24, yellow=24
    8*6=48, 24+24
    
    풀이 과정
    yellow의 면적에 +2 가로 세로 값 구하면 해결
    그 중 brown+yellow 값과 동일한 값 가져오기
    가로가 크므로 그 중 큰 값을 가로로 정하기
    '''
    factors = []
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            factors.append((i, yellow // i))
            
    for pair in factors:
        if (pair[0]+2) * (pair[1]+2) == brown+yellow:
            if pair[0] >= pair[1]:
                return [pair[0]+2, pair[1]+2]
            else:
                return [pair[1]+2, pair[0]+2]
          
          
brown, yellow = 10, 2           
solution(brown, yellow)