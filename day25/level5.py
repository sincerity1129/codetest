def solution(rows, columns, queries):
    '''
    row*columns(행렬) -> 직사각형
    시계방향으로 회전(x1,y1,x2,y2) 한칸씩 회전
    위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열
    
    제한사항
    rows 길이 -> 2 ~ 100
    columns -> 2 ~ 100
    queries의 회전 개수 -> 1 ~ 일만
    
    예시
     1  2  3  4  5  6
     7  8  9 10 11 12
    13 14 15 16 17 18
    19 20 21 22 23 24
    25 26 27 28 29 30
    31 32 33 34 35 36
    
    (2,2,5,4) -> (2,2) (5,4)
    8이 (2,2) // 22이 (5,4)
    (2,2) -> (2,3) -> (2,4) -> (3,4) -> (4,4) -> (5,4) ->
    (5,3) -> (5,2) -> (4,2) -> (3,2) -> (2,2)
    풀이 과정
    1. 이동해야하는 위치 변경
      1) 동일한 x축에서 y축으로 +1만큼 이동
      2) 동일한 y축에서 x축으로 +1만큼 이동
      3) 동일한 x축에서 y축으로 -1만큼 이동
      4) 동일한 y축에서 x축으로 -1만큼 이동
    2. 이동한 위치에 있는 숫자를 리스트로 담아서 min 값 추출
    3. 이걸 지속 반복하면 됨
    4. 리스트 쓰기보다는 딕셔너리로 좌표 값을 키로 해서 값 넣기
    '''
    matrix={}
    value = 1
    for x in range(rows):
        for y in range(columns):
            matrix[(x+1, y+1)] = value
            value+=1
    
    
    answer = []
    for coordinate in queries:
        min_num = 1000000
        x1,y1,x2,y2 = coordinate[0], coordinate[1], coordinate[2], coordinate[3]
        for y_add in range(y1, y2):
            if y_add == y1:
                matrix["now_change_num"] = matrix[(x1, y_add)]
            matrix["after_change_num"] = matrix[(x1, y_add+1)]
            matrix[(x1, y_add+1)] = matrix["now_change_num"]
            min_num = min(min_num, matrix[(x1, y_add+1)])
            matrix["now_change_num"] = matrix["after_change_num"] 
            
        for x_add in range(x1, x2):
            matrix["after_change_num"] = matrix[(x_add+1, y2)]
            matrix[(x_add+1, y2)] = matrix["now_change_num"]
            min_num = min(min_num, matrix[(x_add+1, y2)])
            matrix["now_change_num"] = matrix["after_change_num"] 
            
        for y_sub in range(y2, y1, -1):
            matrix["after_change_num"] = matrix[(x2, y_sub-1)]
            matrix[(x2, y_sub-1)] = matrix["now_change_num"]
            min_num = min(min_num, matrix[(x2, y_sub-1)])
            matrix["now_change_num"] = matrix["after_change_num"] 
            
        for x_sub in range(x2, x1, -1):
            matrix["after_change_num"] = matrix[(x_sub-1, y1)]
            matrix[(x_sub-1, y1)] = matrix["now_change_num"]
            min_num = min(min_num, matrix[(x_sub-1, y1)])
            matrix["now_change_num"] = matrix["after_change_num"] 
        
        answer.append(min_num)
    return answer


rows=6
columns=6	
queries=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

result = solution(rows, columns, queries)
print(result)