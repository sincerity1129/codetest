    # 순서대로 인덱스 나열할 때 규칙 찾아 보자
    # n = 1 -> 0
    # n = 2 -> 0,1,2
    # n = 3 -> 0,1,3,4,2
    # n = 4 -> 0,1,3,6,7,8,9,5,2,4
    # n = 5 -> 0,1,3,6,10,11,12,13,14,9,5,2,4,7
    # n = 6 -> 0,1,3,6,10,15,16,17,18,19,20,14,9,5,2,4,7,11,12,13,8
    
    # 1. 0,1,3,6,10,15 순으로 n-1 개수만큼 늘어남
    # 2. n-1 도달 후 15,16,17,18,19,20 순으로 n-1만큼까지 늘어남
    # 3. 20,14,9,5,2 순서로 값으로 n에서 n-3 줄어듦
    # 4. 2,4,7,11 순서로 n-2 개수만큼 늘어남
    # 5. 11,12,13 n-4 개수만큼 늘어남
    # 6. 13,8 n-2
    
    # n=1 -> 1
    # n=2 -> 1 // 2 + 1
    # n=3 -> 1 // 2 + 4 // 마지막열은 순서대로
    # n=4 -> 1 // 2 + 7 // 3 + 7 - 2 // 마지막열은 순서대로
    # n=5 -> 1 // 2 + 10 // 3 + 10 - 2 // 4 + 10 + 1 + 5 // 마지막열은 순서대로
    # n=6 -> 1 // 2 + 13 // 3 + 13 - 2 // 4 + 13 + 4 - 8 // 5 + 13 + 1 + 1 - 8 // 마지막열은 순서대로
    
    # 방향성 관점에서 보기
    # n=4 -> 아래로 4칸 오른쪽 3칸 후 위 2, 아래 1
    # n=5 -> 아래로 5칸 오른쪽 4칸 후 위 3, 아래 2 오른 1
    # n=6 -> 아래로 6칸 오른쪽 5칸 후 위 4, 아래 3 오른 2, 위 1
    
    # 2차원 배열로 생각해서 행과 열로 생각해보자
    
    # 내려갈 땐 행만 바뀌니까 행 +1, 열 0
    # 오른쪽 할 땐 열이 바뀌니까 행 0, 열 +1
    # 올라갈 땐 행과 열이 각각 바뀌니까 행 -1, 열 -1

n = 8


def snail_move(n, x, y):
    if n % 3 == 0:
        x += 1
    elif n % 3 == 1:
        y += 1
    elif n % 3 == 2:
        x -= 1
        y -= 1
    return x, y
        
snail_matrix = [[1]*(idx+1) for idx in range(n)]

x, y = 0, 0
num = 1
for column in range(len(snail_matrix)):
    for move in range(column, n):
        if move == 0:
            snail_matrix[x][y] = num
            num += 1
            continue
        x, y = snail_move(column, x, y)
        snail_matrix[x][y] = num
        num += 1


print(sum(snail_matrix, []))
