def solution(X, Y):
    '''
    X, Y -> 두 정수(0 ~ 9), 자리수(3 ~ 3백만), 0으로 시작하지 않음 
    동일한 정수가 있으면 묶어주고 이를 활용해서 가장 큰 수를 만들기
    
    예시
    X=3403, Y=13203
    3,0,3이 공통 정수 -> 가장 큰 정수 330
    
    풀이 과정
    자리수를 리스트화
    x 기준으로 리스트 인덱스 pop해서 빼기
    큰 수 정렬해서 문자열로 변환
    
    시간초과 뜨는데 이유는..??
    자리수가 아니라 길이가 3백만까지...리스트가 3백만 개
    count로 값 뽑아내서 개수 순서대로 정렬하면 될 듯
    '''
    X, Y =[x_num for x_num in X], [y_num for y_num in Y]
    same_num = []
    
    # for num in X:
    #     try:
    #         same_num.append(Y.pop(Y.index(num)))
    #     except:
    #         continue
    
    for num in range(9, -1, -1):
        x_count = X.count(str(num))
        y_count = Y.count(str(num))
        
        if  x_count == 0 or y_count == 0:
            continue
        elif x_count >= y_count:
            same_num.append(str(num)*y_count)
        else:
            same_num.append(str(num)*x_count)

    if len(same_num) == 0:
        return "-1"
    elif '0' in same_num[0]:
        return "0"
    answer = ''.join(same_num)
    return answer
    
X, Y = 	"100", "203045"

solution(X, Y)