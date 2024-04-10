def solution(clothes):
    '''
    각 종류별로 최대 1가지 의상만 착용 가능(다만, 동일한 부위에 다른 코디 착용 불가)
    의상 수 -> 1 ~ 30
    같은 이름의 의상 존재X
    각 원소 -> 문자열(1~20길이의 알파벳 소문자 또는 _의 형태)
    
    예시
    clothes = [
    ["yellow_hat", "headgear"], 
    ["blue_sunglasses", "eyewear"], 
    ["green_turban", "headgear"]
    ]
    '''
    # from collections import defaultdict
    # from itertools import combinations
    # clothes_dict = defaultdict(list)
    
    # {clothes_dict[k].append(v) for v, k in clothes}
    
    # clothes_case = [] 
    # for r in range(len(clothes_dict.keys()) + 1):
    #     if r == 0:
    #         continue
    #     clothes_case.extend(list(combinations(clothes_dict.keys(), r)))
        
    # cate_total, item_total =  1, 0
    # for cases in clothes_case:
    #     for key in cases:
    #         if len(cases) <= 1:
    #             item_total += len(clothes_dict[key])
    #             continue
    #         cate_total *= len(clothes_dict[key])
    
    # if len(clothes_dict.keys()) > 1:
    #     return item_total+cate_total
    
    # return item_total
    from collections import defaultdict
    clothes_dict = defaultdict(list)
    {clothes_dict[k].append(v) for v, k in clothes}

    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    answer = 1
    for _, value in clothes_dict.items():
        answer *= (len(value) + 1)

    return answer -1
    
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

answer = solution(clothes)

print(answer)