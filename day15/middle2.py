from itertools import product
answer = 1000*1000
def solution(sizes):
    '''
    명합 지갑을 만드는 회사 -> 지갑의 크기 지정
    1. 60X50 -> 3000
    2. 30X70 -> 2100
    3. 60X30 -> 1800
    4. 80X40 -> 3200
    가로에서 가장 긴 80과 세로에서 가장 긴 50
    80X50 -> 4000
    
    풀이과정 각각 max 값 구해서 곱하면 끝
    '''
    ## 시간 초과
    # all_case = []
    # for cases in list(product(*sizes)):
    #     one_case = []
    #     for case, (w, h) in zip(cases, sizes):
    #         if case == w:
    #             one_case.append([case,h])
    #         else:
    #             one_case.append([case,w])
    #     all_case.append(one_case)
    
    # answer = 1000*1000
    # for cases in all_case:
    #     width, height = 0, 0
    #     for w,h in cases:
    #         width = max(width, w)
    #         height = max(height, h)
    #     answer = min(answer, width*height)
    
    def product_case(sizes, all_case, size_reverse=False):
        global answer
        if len(sizes) == 0:
            width, height = 0, 0
            for w, h in all_case: 
                width = max(width, w)
                height = max(height, h)
            answer = min(answer, width*height)
            return 0
            
        if size_reverse:
            w,h = sizes[0]
            all_case.append([h,w])
        else:
            all_case.append(sizes[0])
        
        product_case(sizes[1:], all_case)
        product_case(sizes[1:], all_case, size_reverse=True)
        if size_reverse:
            all_case.remove([h,w])
        else:
            all_case.remove(sizes[0])
        return answer
        
    all_case = []
    product_case(sizes, all_case)
    product_case(sizes, all_case, size_reverse=True) 
    return answer
        
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
answer = solution(sizes)
print(answer)