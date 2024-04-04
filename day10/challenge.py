'''
바다와 무인도에 대한 정보가 표시
지도는 각 1*1 크기의 사각형
격자의 각 칸 -> X 또는 1~9(자연수)

maps(배열)의 길이 -> 3~100
maps 내의 한 배열의 길이 -> 3~100
maps 내 한 배열의 X 또는 자연수 범위 -> 1~9

maps = ["X591X","X1X5X","X231X", "1XXX1"]
x591x
x1x5x
x231x
1xxx1
5+9+1+1+5+2+3+1 = 27 1, 1// [1,1,27]

maps = ["XXX","XXX","XXX"]
xxx
xxx
xxx
[-1]

풀이과정
maps = ["x2x2", "x3x3", "x1x1", "xxxx"]
x2x2
x313
x1x1
xxxx
예를 위의 코드로 보면
방문한 영역은 다시 가지 않기
4방향으로 이동 가능(위,아래,오른쪽,왼쪽)

'''

def map_move(maps, x, y, n, m, visit):
    area = int(maps[x][y])
    coordinate = [(-1,0),(1,0),(0,-1),(0,1)]
    visit[x][y] = 1
    for dx, dy in coordinate:
        x_move, y_move = x+dx, y+dy
        if 0 <= x_move < n and 0 <= y_move < m and maps[x_move][y_move] !="x" and visit[x_move][y_move] == 0:
            area += map_move(maps, x_move, y_move, n, m, visit)
    return area
            

maps = ["x2x", "x3x", "x11"]
maps = [list(map)for map in maps]
visit = [[0]*len(map) for map in maps]
global answer
answer = []
for x in range(len(maps)):
    for y in range(len(maps[x])):
        if maps[x][y] != 'x':
            answer.append(map_move(maps, x, y, len(maps), len(maps[x]), visit))
        
print(sorted(answer))


import sys
sys.setrecursionlimit(10**5)
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<m
    
    def dfs(x, y):
        nonlocal days
        visited[x][y] = True
        days += int(maps[x][y])
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                dfs(nx, ny)
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                days = 0
                dfs(i, j)
                answer.append(days)
    if not answer:
        answer.append(-1)
    answer = sorted(answer)
    return answer
