def solution(orders, course):
    '''
    코스요리 메뉴 조합(최소 2가지 이상 단품메뉴, 최소 2명 이상의 손님)
    새로 추가하게 될 코스요리의 메뉴 구성 return
    
    제한사항
    orders 길이 -> 2 ~ 20
    orders 원소 길이 -> 2 ~ 10(알파벳 대문자, 중복X)
    course 길이 -> 1 ~ 10
    course 원소 길이 -> 2 ~ 10(오름차순, 중복X)
    return 정렬 오름차순, 많이 주문된 메뉴 구성이 여러 개면 모두 return
    
    예시
    orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course=[2,3,4]
    AC -> 1,2,4,6
    CDE -> 3,4,6
    BCFG -> 1,5
    ACDE -> 4,6
    [AC,ACDE,BCFG,CDE]
    
    풀이과정
    조합에서 가장 많은 개수를 가진 값을 가져옴
    이를 활용해서 result 채우는데 많은 게 동일하면 모두 가져옴
    orders의 메뉴 unique 값을 찾아서 조합 적용
    가장 많은 개수 담기
    '''
    from itertools import combinations
    from collections import Counter
    
    answer = []
    for num in course:
        menu_combo = []
        for menu in orders:
            menu_combo += combinations(sorted(menu), num)
        menu_count = Counter(menu_combo)
        
        if len(menu_count) > 0 and max(menu_count.values()) > 1:
            max_count = 0
            for menu in menu_count:
                max_count = max(menu_count.values())
                if max_count <= menu_count[menu]:
                    answer.append("".join(menu))
    return sorted(answer)


orders=	["XYZ", "XWY", "WXA"]
course=[2,3,4]
solution(orders, course)