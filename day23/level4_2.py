def solution(park, routes):
    '''
    시작 지점 S, 지나다니는 길 O, 장애물 X로 표시된 직사각형 격자 모양의 공원
    park -> 공원을 나타내는 문자열 배열
    routes -> 로봇 강아지가 수행할 명령이 담긴 문자열 배열
    모든 명령 후 놓인 위치
    
    제한사항
    park 길이 -> 3 ~ 50(직사각형 모양)
    park 원소 길이 -> 3 ~ 50
    
    예시
    park=["SOO","OOO","OOO"], routes=["E 2","S 2","W 1"]
    E2 -> ["OOS","OOO","OOO"](오른쪽 2칸)
    S2 -> ["OOO","OOO","OOS"](아래 2칸)
    W1 -> ["OOO","OOO","OSO"](왼쪽 1칸)
    return -> (2,1)
    
    풀이과정
    장애물이 있거나 범위를 벗어난 명령은 적용X
    나머지 명령만 적용
    범위를 벗어났을 때와 장애물 마주치는 경우 패쓰하게 딕셔너리 만들고
    나머지만 이동하게 만들기
    E -> 오른쪽(y+), W -> 왼쪽(y-), N -> 위쪽(x-), S -> 아래쪽(x+)
    '''
    park_dict = {}
    for y, row in enumerate(park):
        for x, column in enumerate(row):
            if column != "S":
                park_dict[(y, x)]=column
            else:
                park_dict[column]=(y,x)
                
    (new_x, new_y) = (0, 0)
    start, end, rule = 0, 0, 0
    for move in routes:
        direction, move = move.split(" ")
        (x, y) = park_dict["S"]
        if direction == "E":
            (new_x, new_y) = (x, y+int(move))
            start, end, rule = y+1, new_y+1, 1
        elif direction == "W":
            (new_x, new_y) = (x, y-int(move))
            start, end, rule = y-1, new_y-1, -1
        elif direction == "S":
            (new_x, new_y) = (x+int(move), y)
            start, end, rule = x+1, new_x+1, 1
        elif direction == "N":
            (new_x, new_y) = (x-int(move), y)
            start, end, rule = x-1, new_x-1, -1

        try:
            (check_x, check_y) = (0,0)
            move_range = (end-start)
            for idx in range(start, end, rule):
                if direction == "E" or direction == "W":
                    if y + move_range > len(park[0])-1 or y + move_range < 0:
                        break
                    (check_x, check_y) = (x, idx)
                else:
                    if x + move_range > len(park[0])-1 or x + move_range < 0:
                        break
                    (check_x, check_y) = (idx, y)
                if park_dict[(check_x, check_y)] == "X":
                    break
                
                if idx == end-1 or idx == end+1:
                    park_dict[(x, y)] = "O"
                    park_dict["S"] = (check_x, check_y)
        except:
            continue
    
    return list(park_dict["S"])

# park=["SOO", "OXX", "OOO"]
# routes=["E 2", "S 2", "W 1"]

park=["OSO", "OOO", "OXO", "OOO"]
routes=["E 2", "S 3", "W 1"]

result = solution(park, routes)
print(result)