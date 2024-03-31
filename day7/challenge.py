from itertools import permutations

'''
피로도 시스템 -> 0이상의 정수로 표현
최소 필요 피로도와 소모 피로도 모든 조건 만족(2차원 배열)
유저가 탐험할 수 있는 최대 던전 수를 return

유저 현재 피로도 k -> 1~5000
dungeons(2차원 배열) -> 행 1~8, 열 2
dungeons 각 행[최소 필요 피로도, 소모 피로도](1~1000 자연수)
최소 필요 피로도 >= 소모 피로도
던전의 조건에서 최소 필요 피로도와 소모 피로도가 같을 수 있음

k = 80
dungeons -> 80,20 // 50,40 // 30,10
80 -> (80,20) -> 60 -> (30, 10) -> 50 -> (50, 40)

주어진 내용으로 확인해 볼 때
최소 필요 피로도 기준으로 나열
소모 피로도도 소모 이후에 최소한으로 최소 필요 피로도 소모하는 결과 확인
이 과정을 지속하면 결과 도출



다른 방법 생각해 보기
모든 경우의 수를 가져와서 하나씩 대입하면서 해보기

'''

k = 80
dungeons = [[80, 20], [50,40], [30,10]]

dungeons_permutation = list(permutations(dungeons,len(dungeons)))  

max_score = 0
for dungeons_case in dungeons_permutation:
    case_count = 0
    basic_fatigue = k

    for dungeon in dungeons_case:
        if basic_fatigue >= dungeon[0]:
            basic_fatigue -= dungeon[1]
            case_count += 1
        elif basic_fatigue <= 0:
            break
        max_score = max(case_count, max_score)
        
    if max_score == len(dungeons_case):
        break

print(max_score)