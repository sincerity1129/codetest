def solution(n, k, enemy):
    '''
    n = 병사의 수
    enemy = 적의 수
    k = 라운드 패쓰권 개수
    
    n=7, k=3, enemy=[4, 2, 4, 5, 3, 3, 1]
    1,3,5 -> 패쓰권 사용, 2,4 -> 2,5 병사 소모
    5라운드까지 가능
    
    풀이과정
    완전탐색인가? 경우의 수마다 다 적용해서 최적의 값을 찾는 것 같음
    며칠 전에 했던 던전 최대치 같은 느낌
    재귀함수를 써서 모든 경우의 수 모두 확인해서 최고 값 찾아 내기
    
    결론은 실패
    완전 탐색 아니고 힙을 쓰는 방식이었음..
    
    다른 방식 풀이
    정렬해서 가장 큰 값을 빼주는 방식으로 진행
    리스트 값 담아주고 큰 값 뺄 때 K 값 -1
    '''
    mob_list = []
    mob_count, answer = 0, 0
    for mob in enemy:
        mob_list.append(mob)
        mob_count += mob
        if mob_count > n:
            if k ==0: break
            k -= 1 
            mob_count = sum(mob_list) - mob_list.pop(mob_list.index(max(mob_list)))
        answer += 1

    return answer


# n=7 
# k=3
# enemy=[4, 2, 4, 5, 3, 3, 1]
n=2	
k=4	
enemy=[3, 3, 3, 3]
answer = solution(n, k, enemy)

print(answer)